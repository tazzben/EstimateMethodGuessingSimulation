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
	if numoptions >= 1:
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
	if numoptions >= 1:
		egamma = (1-nl-pl*numoptions-rl)/((numoptions-1)*(nl+rl-1))
		return egamma
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
		df['gammagain'] = df['gamma']/(1-df['mu'])
		df['egamma'] = df.apply(Gamma,args=(gprob,),axis=1)
		df['egammagain'] = df.apply(GammaGain,args=(gprob,),axis=1)
		df['engamma'] = -1*(((df['nl']-df['pl'])*(df['pl']+df['rl']-1))/(df['nl']+df['pl']+df['rl']-1))
		df['engammagain'] = (df['pl']-df['nl'])/(1-df['nl']-df['rl'])
		questions = questions.append(df, ignore_index=True)
		d = sqldf('SELECT id, AVG(pl) AS pl, AVG(zl) AS zl, AVG(rl) AS rl, AVG(nl) AS nl, AVG(gamma) AS gamma, AVG(alpha) AS alpha, AVG(mu) AS mu, AVG(gammagain) AS gammagain, AVG(egamma) AS egamma, AVG(egammagain) AS egammagain, AVG(engamma) AS engamma, AVG(engammagain) AS engammagain FROM df',locals())
		df2 = pd.DataFrame(d)
		classes = classes.append(df2, ignore_index=True)
	
	questions['esq'] = (questions['gamma'] - questions['egamma'])**2
	questions['eabs'] = (questions['gamma'] - questions['egamma']).abs()
	questions['eper'] = ((questions['gamma'] - questions['egamma'])/questions['gamma'])
	questions['eperabs'] = questions['eper'].abs()
	questions['epersq'] = (questions['eper'])**2
	questions['egainsq'] = (questions['gammagain'] - questions['egammagain'])**2
	questions['egainabs'] = (questions['gammagain'] - questions['egammagain']).abs()
	questions['egainper'] = ((questions['gammagain'] - questions['egammagain'])/questions['gammagain'])
	questions['egainperabs'] = questions['egainper'].abs()
	questions['egainpersq'] = (questions['egainper'])**2
	
	questions['eperzero'] = ((questions['gamma'] - questions['engamma'])/questions['gamma'])
	questions['eperzeroabs'] = questions['eperzero'].abs()
	questions['eperzerosq'] = (questions['eperzero'])**2	
	questions['esqzero'] = (questions['gamma'] - questions['engamma'])**2
	questions['eabszero'] = (questions['gamma'] - questions['engamma']).abs()
	questions['egainsqzero'] = (questions['gammagain'] - questions['engammagain'])**2
	questions['egainabszero'] = (questions['gammagain'] - questions['engammagain']).abs()
	questions['egainperzero'] = ((questions['gammagain'] - questions['engammagain'])/questions['gammagain'])
	questions['egainperzeroabs'] = questions['egainperzero'].abs()
	questions['egainperzerosq'] = (questions['egainperzero'])**2
	
	classes['eper'] = ((classes['gamma'] - classes['egamma'])/classes['gamma'])
	classes['eperabs'] = classes['eper'].abs()
	classes['epersq'] = (classes['eper'])**2
	classes['esq'] = (classes['gamma'] - classes['egamma'])**2
	classes['eabs'] = (classes['gamma'] - classes['egamma']).abs()
	classes['egainsq'] = (classes['gammagain'] - classes['egammagain'])**2
	classes['egainabs'] = (classes['gammagain'] - classes['egammagain']).abs()
	classes['egainper'] = ((classes['gammagain'] - classes['egammagain'])/classes['gammagain'])
	classes['egainpersq'] = (classes['egainper'])**2
	classes['egainperabs'] = classes['egainper'].abs()
	classes['eperzero'] = ((classes['gamma'] - classes['engamma'])/classes['gamma'])
	classes['eperzeroabs'] = classes['eperzero'].abs()
	classes['eperzerosq'] = (classes['eperzero'])**2
	classes['esqzero'] = (classes['gamma'] - classes['engamma'])**2
	classes['eabszero'] = (classes['gamma'] - classes['engamma']).abs()
	classes['egainsqzero'] = (classes['gammagain'] - classes['engammagain'])**2
	classes['egainabszero'] = (classes['gammagain'] - classes['engammagain']).abs()
	classes['egainperzero'] = ((classes['gammagain'] - classes['engammagain'])/classes['gammagain'])
	classes['egainperzeroabs'] = classes['egainperzero'].abs()
	classes['egainperzerosq'] = (classes['egainperzero'])**2 
	
	return (classes, questions)


def ManageSimulation(reps, q, n, mu, alpha, gamma, prob, gprob):
	classes, questions = SimulateDist(reps, q, n, mu, alpha, gamma, prob, gprob)
	classaverage = sqldf("SELECT AVG(esq) AS esq, AVG(eabs) AS eabs, AVG(egainsq) AS egainsq, AVG(egainabs) AS egainabs, AVG(esqzero) AS esqzero, AVG(eabszero) AS eabszero, AVG(egainsqzero) AS egainsqzero, AVG(egainabszero) AS egainabszero, AVG(egamma) AS egamma, AVG(egammagain) AS egammagain, AVG(engamma) AS engamma, AVG(engammagain) AS engammagain, AVG(gammagain) AS gammagain, AVG(gamma) AS gamma, AVG(eper) AS eper, AVG(eperabs) AS eperabs, AVG(epersq) AS epersq, AVG(egainper) AS egainper, AVG(egainperabs) AS egainperabs, AVG(egainpersq) AS egainpersq, AVG(eperzero) AS eperzero, AVG(eperzeroabs) AS eperzeroabs, AVG(eperzerosq) AS eperzerosq, AVG(egainperzero) AS egainperzero,   AVG(egainperzeroabs) AS egainperzeroabs, AVG(egainperzerosq) AS egainperzerosq FROM classes",locals())
	qaverage = sqldf("SELECT AVG(esq) AS esq, AVG(eabs) AS eabs, AVG(egainsq) AS egainsq, AVG(egainabs) AS egainabs, AVG(esqzero) AS esqzero, AVG(eabszero) AS eabszero, AVG(egainsqzero) AS egainsqzero, AVG(egainabszero) AS egainabszero, AVG(eper) AS eper, AVG(eperabs) AS eperabs, AVG(epersq) AS epersq, AVG(egainper) AS egainper, AVG(egainperabs) AS egainperabs, AVG(egainpersq) AS egainpersq, AVG(eperzero) AS eperzero, AVG(eperzeroabs) AS eperzeroabs, AVG(eperzerosq) AS eperzerosq, AVG(egainperzero) AS egainperzero,   AVG(egainperzeroabs) AS egainperzeroabs, AVG(egainperzerosq) AS egainperzerosq FROM questions WHERE question=1",locals())
	return classaverage, qaverage


def ManageProcess(row):
	try:
		classaverage, qaverage = ManageSimulation(row['reps'], row['questions'], row['studs'], row['mu'], row['alpha'], row['gamma'], row['prob'], row['guessprob'])
		return {'mu':row['mu'],'alpha':row['alpha'],'gamma':row['gamma'],'prob':row['prob'],'studs':row['studs'],'ClassEstSq':float(classaverage['esq'].astype(float)),'ClassEstAbs':float(classaverage['eabs'].astype(float)),'ClassEstGainSq':float(classaverage['egainsq'].astype(float)),'ClassEstGainAbs':float(classaverage['egainabs'].astype(float)),'ClassEstZeroSq':float(classaverage['esqzero'].astype(float)),'ClassEstZeroAbs':float(classaverage['eabszero'].astype(float)),'ClassEstGainZeroSq':float(classaverage['egainsqzero'].astype(float)),'ClassEstGainZeroAbs':float(classaverage['egainabszero'].astype(float)),'EstGamma':float(classaverage['egamma'].astype(float)),'EstGammaGain':float(classaverage['egammagain'].astype(float)),'EstGammaZero':float(classaverage['engamma'].astype(float)),'EstGammaGainZero':float(classaverage['engammagain'].astype(float)),'AvgGamma':float(classaverage['gamma'].astype(float)),'AvgGammaGain':float(classaverage['gammagain'].astype(float)),'QuestionEstSq':float(qaverage['esq'].astype(float)),'QuestionEstAbs':float(qaverage['eabs'].astype(float)),'QuestionEstGainSq':float(qaverage['egainsq'].astype(float)),'QuestionEstGainAbs':float(qaverage['egainabs'].astype(float)),'QuestionEstZeroSq':float(qaverage['esqzero'].astype(float)),'QuestionEstZeroAbs':float(qaverage['eabszero'].astype(float)),'QuestionEstGainZeroSq':float(qaverage['egainsqzero'].astype(float)),'QuestionEstGainZeroAbs':float(qaverage['egainabszero'].astype(float)),'ClassEstGammaAvgPercentChange':float(classaverage['eper'].astype(float)),'ClassEstGammaAvgAbsPercentChange':float(classaverage['eperabs'].astype(float)),'ClassEstGammaAvgSqPercentChange':float(classaverage['epersq'].astype(float)),'ClassEstGainAvgPercentChange':float(classaverage['egainper'].astype(float)),'ClassEstGainAvgAbsPercentChange':float(classaverage['egainperabs'].astype(float)),'ClassEstGainAvgSqPercentChange':float(classaverage['egainpersq'].astype(float)),'ClassEstGammaZeroAvgPercentChange':float(classaverage['eperzero'].astype(float)),'ClassEstGammaZeroAvgAbsPercentChange':float(classaverage['eperzeroabs'].astype(float)),'ClassEstGammaZeroAvgSqPercentChange':float(classaverage['eperzerosq'].astype(float)),'ClassEstGainZeroAvgPercentChange':float(classaverage['egainperzero'].astype(float)),'ClassEstGainZeroAvgAbsPercentChange':float(classaverage['egainperzeroabs'].astype(float)),'ClassEstGainZeroAvgSqPercentChange':float(classaverage['egainperzerosq'].astype(float)),'QuestionEstGammaAvgPercentChange':float(qaverage['eper'].astype(float)),'QuestionEstGammaAvgAbsPercentChange':float(qaverage['eperabs'].astype(float)),'QuestionEstGammaAvgSqPercentChange':float(qaverage['epersq'].astype(float)),'QuestionEstGainAvgPercentChange':float(qaverage['egainper'].astype(float)),'QuestionEstGainAvgAbsPercentChange':float(qaverage['egainperabs'].astype(float)),'QuestionEstGainAvgSqPercentChange':float(qaverage['egainpersq'].astype(float)),'QuestionEstGammaZeroAvgPercentChange':float(qaverage['eperzero'].astype(float)),'QuestionEstGammaZeroAvgAbsPercentChange':float(qaverage['eperzeroabs'].astype(float)),'QuestionEstGammaZeroAvgSqPercentChange':float(qaverage['eperzerosq'].astype(float)),'QuestionEstGainZeroAvgPercentChange':float(qaverage['egainperzero'].astype(float)),'QuestionEstGainZeroAvgAbsPercentChange':float(qaverage['egainperzeroabs'].astype(float)),'QuestionEstGainZeroAvgSqPercentChange':float(qaverage['egainperzerosq'].astype(float))}
	except:
		return {'mu':row['mu'],'alpha':row['alpha'],'gamma':row['gamma'],'prob':row['prob'],'studs':row['studs'],'ClassEstSq':None,'ClassEstAbs':None,'ClassEstGainSq':None,'ClassEstGainAbs':None,'ClassEstZeroSq':None,'ClassEstZeroAbs':None,'ClassEstGainZeroSq':None,'ClassEstGainZeroAbs':None,'EstGamma':None,'EstGammaGain':None,'EstGammaZero':None,'EstGammaGainZero':None,'AvgGamma':None,'AvgGammaGain':None,'QuestionEstSq':None,'QuestionEstAbs':None,'QuestionEstGainSq':None,'QuestionEstGainAbs':None,'QuestionEstZeroSq':None,'QuestionEstZeroAbs':None,'QuestionEstGainZeroSq':None,'QuestionEstGainZeroAbs':None,'ClassEstGammaAvgPercentChange':None,'ClassEstGammaAvgAbsPercentChange':None,'ClassEstGammaAvgSqPercentChange':None,'ClassEstGainAvgPercentChange':None,'ClassEstGainAvgAbsPercentChange':None,'ClassEstGainAvgSqPercentChange':None,'ClassEstGammaZeroAvgPercentChange':None,'ClassEstGammaZeroAvgAbsPercentChange':None,'ClassEstGammaZeroAvgSqPercentChange':None,'ClassEstGainZeroAvgPercentChange':None,'ClassEstGainZeroAvgAbsPercentChange':None,'ClassEstGainZeroAvgSqPercentChange':None,'QuestionEstGammaAvgPercentChange':None,'QuestionEstGammaAvgAbsPercentChange':None,'QuestionEstGammaAvgSqPercentChange':None,'QuestionEstGainAvgPercentChange':None,'QuestionEstGainAvgAbsPercentChange':None,'QuestionEstGainAvgSqPercentChange':None,'QuestionEstGammaZeroAvgPercentChange':None,'QuestionEstGammaZeroAvgAbsPercentChange':None,'QuestionEstGammaZeroAvgSqPercentChange':None,'QuestionEstGainZeroAvgPercentChange':None,'QuestionEstGainZeroAvgAbsPercentChange':None,'QuestionEstGainZeroAvgSqPercentChange':None}
	

if __name__ == '__main__':
#	mulist = [.1, .3, .5, .7]
#	alphalist = [.01, .03, .05, .07, .09]
#	gammalist = [.1, .3, .5]
#	problist = [.15, .2, .25, .3, .35, .50]
#	studs = [15, 30, 50, 100]
#	reps = 10000
	
	mulist = [.1, .3,]
	alphalist = [.01,]
	gammalist = [.1,]
	problist = [.15,]
	studs = [15, ]
	reps = 10

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
	with open('results.csv', 'w') as output_file:
		dict_writer = csv.DictWriter(output_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(r)