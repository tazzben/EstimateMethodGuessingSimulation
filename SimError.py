#!/usr/bin/env python
from __future__ import division, print_function, absolute_import
import os
import sys
import csv
import numpy
import pandas as pd
import argparse
from pandasql import sqldf
from multiprocessing import Pool
from itertools import product

def GuessPre(x, prob):
	if x['mu']==1:
		return 1
	if numpy.random.uniform(0,1) <= prob:
		return 1
	else:
		return 0

def GuessPost(x, prob):
	if (x['mu']==1 and x['alpha']==0) or x['gamma']==1:
		return 1
	if numpy.random.uniform(0,1) <= prob:
		return 1
	else:
		return 0

def NL(x):
	if x['posttest']==0 and x['pretest']==1:
		return 1
	else:
		return 0

def PL(x):
	if x['posttest']==1 and x['pretest']==0:
		return 1
	else:
		return 0

def ZL(x):
	if x['posttest']==0 and x['pretest']==0:
		return 1
	else:
		return 0

def RL(x):
	if x['posttest']==1 and x['pretest']==1:
		return 1
	else:
		return 0

def Gamma(x, gprob):
	pl = x['pl']
	zl = x['zl']
	rl = x['rl']
	nl = x['nl']
	numoptions = 1/gprob
	if numoptions >= 1 and ((numoptions-1)**2) != 0:
		egamma = (numoptions*(nl+pl*numoptions+rl-1))/((numoptions-1)**2)
		return egamma
	else:
		return None

def GammaGain(x, gprob):
	pl = x['pl']
	zl = x['zl']
	rl = x['rl']
	nl = x['nl']
	numoptions = 1/gprob
	if numoptions >= 1 and ((numoptions-1)*(nl+rl-1)) != 0:
		egamma = (1-nl-pl*numoptions-rl)/((numoptions-1)*(nl+rl-1))
		return egamma
	else:
		return None

def ZeroGamma(x):
	if (x['nl']+x['pl']+x['rl']-1) != 0:
		ezgamma = -1*(((x['nl']-x['pl'])*(x['pl']+x['rl']-1))/(x['nl']+x['pl']+x['rl']-1))
		return ezgamma
	else:
		return None
		
def ZeroGammaGain(x):
	if (1-x['nl']-x['rl']) != 0:
		ezgamma = (x['pl']-x['nl'])/(1-x['nl']-x['rl'])
		return ezgamma
	else:
		return None
		
def CGammaGain(x):
	if (1-x['mu']) != 0:
		return x['gamma']/(1-x['mu'])
	else:
		return None		

def GetStudents(mu, q, n, alpha, gamma):
	studentability = numpy.random.binomial(q, mu, size=n)
	gamma = gamma/(1-mu)
	alpha = alpha/mu
	studentid = 0
	StudentClass = pd.DataFrame(columns=('mu', 'alpha', 'gamma','question','studentid'))
	for student in studentability:
		studentid = studentid + 1
		knownResponses = numpy.concatenate((numpy.ones(student),numpy.zeros(q - student)))
		studentforgot = numpy.random.binomial(student, alpha)
		forgotResponses = numpy.concatenate((numpy.ones(studentforgot),numpy.zeros(q - studentforgot)))
		studentlearned = numpy.random.binomial(q - student, gamma)
		learnedResponses = numpy.concatenate((numpy.zeros(q - studentlearned),numpy.ones(studentlearned)))
		studentK = numpy.column_stack((knownResponses, forgotResponses, learnedResponses))
		numpy.random.shuffle(studentK)
		df = pd.DataFrame(data=studentK,columns=('mu','alpha','gamma'))
		df['question'] = pd.Series(numpy.arange(1,q+1), index=df.index)
		df['studentid'] = studentid
		StudentClass = StudentClass.append(df,ignore_index=True)
	return StudentClass



def SimulateDist(reps, q, n, mu, alpha, gamma, prob, gprob):
	gammagainc = gamma/(1-mu)
	questions = pd.DataFrame(columns=('id','question', 'pl', 'zl', 'rl', 'nl', 'gamma','alpha','mu','gammagain','egamma','egammagain','engamma','engammagain'))
	classes = pd.DataFrame(columns=('id','pl', 'zl', 'rl', 'nl', 'gamma','alpha','mu','gammagain','egamma','egammagain','engamma','engammagain'))
	for i in range(reps):
		students = GetStudents(mu, q, n, alpha, gamma)
		students['pretest'] = students.apply(GuessPre, args=(prob,), axis=1)
		students['posttest'] = students.apply(GuessPost, args=(prob,), axis=1)
		students['pl'] = students.apply(PL, axis=1)
		students['nl'] = students.apply(NL, axis=1)
		students['zl'] = students.apply(ZL, axis=1)
		students['rl'] = students.apply(RL, axis=1)
		d = sqldf('SELECT question, AVG(pl) AS pl, AVG(zl) AS zl, AVG(rl) AS rl, AVG(nl) AS nl, AVG(gamma) AS gamma, AVG(alpha) AS alpha, AVG(mu) AS mu FROM students GROUP BY question',locals())
		df = pd.DataFrame(d)
		df['id'] = i
		df['gammagain'] = df.apply(CGammaGain,axis=1)
		df['egamma'] = df.apply(Gamma,args=(gprob,),axis=1)
		df['egammagain'] = df.apply(GammaGain,args=(gprob,),axis=1)
		df['engamma'] = df.apply(ZeroGamma,axis=1)
		df['engammagain'] = df.apply(ZeroGammaGain,axis=1)
		questions = questions.append(df, ignore_index=True)
		d = sqldf('SELECT id, AVG(pl) AS pl, AVG(zl) AS zl, AVG(rl) AS rl, AVG(nl) AS nl, AVG(gamma) AS gamma, AVG(alpha) AS alpha, AVG(mu) AS mu, AVG(gammagain) AS gammagain, AVG(egamma) AS egamma, AVG(egammagain) AS egammagain, AVG(engamma) AS engamma, AVG(engammagain) AS engammagain FROM df',locals())
		df2 = pd.DataFrame(d)
		classes = classes.append(df2, ignore_index=True)
	
	questions['eabs'] = (questions['gamma'] - questions['egamma']).abs()
	questions['egainabs'] = (questions['gammagain'] - questions['egammagain']).abs()
	questions['eabszero'] = (questions['gamma'] - questions['engamma']).abs()
	questions['egainabszero'] = (questions['gammagain'] - questions['engammagain']).abs()
	
	classes['eabs'] = (classes['gamma'] - classes['egamma']).abs()
	classes['egainabs'] = (classes['gammagain'] - classes['egammagain']).abs()
	classes['eabszero'] = (classes['gamma'] - classes['engamma']).abs()
	classes['egainabszero'] = (classes['gammagain'] - classes['engammagain']).abs()
	
	return (classes, questions)


def ManageSimulation(reps, q, n, mu, alpha, gamma, prob, gprob):
	classes, questions = SimulateDist(reps, q, n, mu, alpha, gamma, prob, gprob)
	classaverage = sqldf("SELECT AVG(eabs) AS eabs, AVG(egainabs) AS egainabs, AVG(eabszero) AS eabszero, AVG(egainabszero) AS egainabszero, AVG(egamma) AS egamma, AVG(egammagain) AS egammagain, AVG(engamma) AS engamma, AVG(engammagain) AS engammagain, AVG(gammagain) AS gammagain, AVG(gamma) AS gamma FROM classes",locals())
	qaverage = sqldf("SELECT AVG(eabs) AS eabs, AVG(egainabs) AS egainabs, AVG(eabszero) AS eabszero, AVG(egainabszero) AS egainabszero, AVG(egamma) AS egamma, AVG(egammagain) AS egammagain, AVG(engamma) AS engamma, AVG(engammagain) AS engammagain, AVG(gammagain) AS gammagain, AVG(gamma) AS gamma FROM questions WHERE question=1",locals())
	return classaverage, qaverage


def ManageProcess(row):
	try:
		classaverage, qaverage = ManageSimulation(row['reps'], row['questions'], row['studs'], row['mu'], row['alpha'], row['gamma'], row['prob'], row['guessprob'])
		return {'mu':row['mu'],'alpha':row['alpha'],'gamma':row['gamma'],'prob':row['prob'],'studs':row['studs'],'ClassEstAbs':float(classaverage['eabs'].astype(float)),'ClassEstGainAbs':float(classaverage['egainabs'].astype(float)),'ClassEstZeroAbs':float(classaverage['eabszero'].astype(float)),'ClassEstGainZeroAbs':float(classaverage['egainabszero'].astype(float)),'QuestionEstAbs':float(qaverage['eabs'].astype(float)),'QuestionEstGainAbs':float(qaverage['egainabs'].astype(float)),'QuestionEstZeroAbs':float(qaverage['eabszero'].astype(float)),'QuestionEstGainZeroAbs':float(qaverage['egainabszero'].astype(float))}
	except:
		return {'mu':row['mu'],'alpha':row['alpha'],'gamma':row['gamma'],'prob':row['prob'],'studs':row['studs'],'ClassEstAbs':None,'ClassEstGainAbs':None,'ClassEstZeroAbs':None,'ClassEstGainZeroAbs':None,'QuestionEstAbs':None,'QuestionEstGainAbs':None,'QuestionEstZeroAbs':None,'QuestionEstGainZeroAbs':None}
	

if __name__ == '__main__':
	mulist = [.1, .2, .3, .4, .5]
	alphalist = [.01, .02, .03, .04, .05]
	gammalist = [.1, .2, .3, .4, .5]
	problist = [.15, .2, .25, .3, .35]
	studs = [30, 50, 100]
	reps = 10000
	
#	mulist = [.1, .3,]
#	alphalist = [.01,]
#	gammalist = [.1,]
#	problist = [.15,]
#	studs = [30,]
#	reps = 100

	questions = 30
	guessprob = 0.25

	combs=pd.DataFrame(list(product(mulist, alphalist, gammalist, problist, studs)), columns=['mu', 'alpha', 'gamma', 'prob', 'studs'])
	combs = combs[((combs['mu']+combs['alpha']+combs['gamma'])<1)]
	interList = []
	for _, row in combs.iterrows():
		interList.append({'mu':float(row['mu'].astype(float)),'alpha':float(row['alpha'].astype(float)),'gamma':float(row['gamma'].astype(float)),'prob':float(row['prob'].astype(float)),'studs':int(row['studs']),'reps':reps,'questions':questions,'guessprob':guessprob})
	
	p = Pool()
	r = p.map(ManageProcess, interList)
	p.close()
	p.join()
	keys = r[0].keys()
	fields = ['mu','alpha','gamma','prob','studs','ClassEstAbs','ClassEstGainAbs','ClassEstZeroAbs','ClassEstGainZeroAbs','QuestionEstAbs','QuestionEstGainAbs','QuestionEstZeroAbs','QuestionEstGainZeroAbs']
	with open('results.csv', 'w') as output_file:
		dict_writer = csv.DictWriter(output_file, fieldnames=fields)
		dict_writer.writeheader()
		dict_writer.writerows(r)