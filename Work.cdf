(* Content-type: application/vnd.wolfram.cdf.text *)

(*** Wolfram CDF File ***)
(* http://www.wolfram.com/cdf *)

(* CreatedBy='Mathematica 11.2' *)

(***************************************************************************)
(*                                                                         *)
(*                                                                         *)
(*  Under the Wolfram FreeCDF terms of use, this file and its content are  *)
(*  bound by the Creative Commons BY-SA Attribution-ShareAlike license.    *)
(*                                                                         *)
(*        For additional information concerning CDF licensing, see:        *)
(*                                                                         *)
(*         www.wolfram.com/cdf/adopting-cdf/licensing-options.html         *)
(*                                                                         *)
(*                                                                         *)
(***************************************************************************)

(*CacheID: 234*)
(* Internal cache information:
NotebookFileLineBreakTest
NotebookFileLineBreakTest
NotebookDataPosition[      1088,         20]
NotebookDataLength[     16335,        517]
NotebookOptionsPosition[     14011,        462]
NotebookOutlinePosition[     14371,        478]
CellTagsIndexPosition[     14328,        475]
WindowFrame->Normal*)

(* Beginning of Notebook Content *)
Notebook[{

Cell[CellGroupData[{
Cell["\<\
Store the original Smith and Wagner estimators and restate them in terms of \
estimated probability (ep) instead of n; Specify the gain estimator\
\>", "Subsection",
 CellChangeTimes->{{3.722761416839746*^9, 3.722761451380097*^9}, {
  3.722761649451442*^9, 
  3.722761672201889*^9}},ExpressionUUID->"f2aa9cf8-4cfb-4b41-8681-\
a5a68cc52e2b"],

Cell[CellGroupData[{

Cell[BoxData[{
 RowBox[{"mu", " ", "=", " ", 
  RowBox[{"Simplify", "[", 
   RowBox[{
    RowBox[{"enl", "+", "erl", "+", 
     FractionBox[
      RowBox[{
       RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], 
      RowBox[{
       RowBox[{"-", "1"}], "+", "n"}]]}], "/.", " ", 
    RowBox[{"n", "\[Rule]", 
     RowBox[{"1", "/", "ep"}]}]}], "]"}]}], "\[IndentingNewLine]", 
 RowBox[{"gamma", " ", "=", 
  RowBox[{"Simplify", "[", " ", 
   RowBox[{
    FractionBox[
     RowBox[{"n", " ", 
      RowBox[{"(", 
       RowBox[{
        RowBox[{"-", "1"}], "+", "enl", "+", "erl", "+", 
        RowBox[{"epl", " ", "n"}]}], ")"}]}], 
     SuperscriptBox[
      RowBox[{"(", 
       RowBox[{
        RowBox[{"-", "1"}], "+", "n"}], ")"}], "2"]], "/.", 
    RowBox[{"n", "\[Rule]", 
     RowBox[{"1", "/", "ep"}]}]}], "]"}]}], "\[IndentingNewLine]", 
 RowBox[{"alpha", " ", "=", " ", 
  RowBox[{"Simplify", "[", 
   RowBox[{
    FractionBox[
     RowBox[{"n", " ", 
      RowBox[{"(", 
       RowBox[{
        RowBox[{"-", "1"}], "+", "epl", "+", "erl", "+", 
        RowBox[{"enl", " ", "n"}]}], ")"}]}], 
     SuperscriptBox[
      RowBox[{"(", 
       RowBox[{
        RowBox[{"-", "1"}], "+", "n"}], ")"}], "2"]], "/.", " ", 
    RowBox[{"n", "\[Rule]", 
     RowBox[{"1", "/", "ep"}]}]}], "]"}]}], "\[IndentingNewLine]", 
 RowBox[{"gain", " ", "=", " ", 
  RowBox[{"Simplify", "[", 
   FractionBox["gamma", 
    RowBox[{"1", "-", "mu"}]], "]"}]}]}], "Input",
 CellChangeTimes->{{3.722760749977314*^9, 
  3.722760861591363*^9}},ExpressionUUID->"d5918e45-489a-492c-a04c-\
e9d1b8ee1e68"],

Cell[BoxData[
 FractionBox[
  RowBox[{"enl", "-", "ep", "+", "erl"}], 
  RowBox[{"1", "-", "ep"}]]], "Output",
 CellChangeTimes->{
  3.722760810415648*^9, {3.72276084326712*^9, 3.72276086217373*^9}, 
   3.722761378625256*^9},ExpressionUUID->"704f7289-3090-4724-82d9-\
d45c63aa0226"],

Cell[BoxData[
 FractionBox[
  RowBox[{"epl", "+", 
   RowBox[{"ep", " ", 
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], ")"}]}]}], 
  SuperscriptBox[
   RowBox[{"(", 
    RowBox[{
     RowBox[{"-", "1"}], "+", "ep"}], ")"}], "2"]]], "Output",
 CellChangeTimes->{
  3.722760810415648*^9, {3.72276084326712*^9, 3.72276086217373*^9}, 
   3.722761378636286*^9},ExpressionUUID->"b0501a5c-ad47-44ca-a219-\
7b8734897053"],

Cell[BoxData[
 FractionBox[
  RowBox[{"enl", "+", 
   RowBox[{"ep", " ", 
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "epl", "+", "erl"}], ")"}]}]}], 
  SuperscriptBox[
   RowBox[{"(", 
    RowBox[{
     RowBox[{"-", "1"}], "+", "ep"}], ")"}], "2"]]], "Output",
 CellChangeTimes->{
  3.722760810415648*^9, {3.72276084326712*^9, 3.72276086217373*^9}, 
   3.722761378644045*^9},ExpressionUUID->"42757dde-b5fb-4727-8c80-\
51cb15ae704c"],

Cell[BoxData[
 FractionBox[
  RowBox[{"epl", "+", 
   RowBox[{"ep", " ", 
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], ")"}]}]}], 
  RowBox[{
   RowBox[{"(", 
    RowBox[{
     RowBox[{"-", "1"}], "+", "ep"}], ")"}], " ", 
   RowBox[{"(", 
    RowBox[{
     RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], ")"}]}]]], "Output",
 CellChangeTimes->{
  3.722760810415648*^9, {3.72276084326712*^9, 3.72276086217373*^9}, 
   3.7227613786516933`*^9},ExpressionUUID->"d95acf38-b1c1-4239-bf3f-\
8c09177aced0"]
}, Open  ]]
}, Open  ]],

Cell[CellGroupData[{

Cell["\<\
Solve for implied probability when alpha =0; Substitute the value into the \
gamma and gain estimator\
\>", "Subsection",
 CellChangeTimes->{{3.722761467789064*^9, 
  3.7227615116653967`*^9}},ExpressionUUID->"00241716-2ee5-4097-bd88-\
2726d900d23d"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"nls", " ", "=", 
  RowBox[{"Flatten", "[", 
   RowBox[{"Solve", "[", 
    RowBox[{
     RowBox[{"alpha", "\[Equal]", "0"}], ",", "ep"}], "]"}], "]"}]}]], "Input",\

 CellChangeTimes->{{3.72276125067773*^9, 
  3.722761276526635*^9}},ExpressionUUID->"012ea6d7-faf4-49f5-8619-\
7fcf63319552"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"ep", "\[Rule]", 
   RowBox[{"-", 
    FractionBox["enl", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "epl", "+", "erl"}]]}]}], "}"}]], "Output",
 CellChangeTimes->{{3.722761256510442*^9, 3.722761276896957*^9}, 
   3.722761378726495*^9},ExpressionUUID->"bf88be53-797b-4e78-95c3-\
7fe5f505d98c"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[{
 RowBox[{"gammaZ", " ", "=", " ", 
  RowBox[{"Simplify", "[", 
   RowBox[{"gamma", " ", "/.", " ", "nls"}], "]"}]}], "\[IndentingNewLine]", 
 RowBox[{"gainZ", " ", "=", " ", 
  RowBox[{"Simplify", "[", 
   RowBox[{"gain", " ", "/.", "nls"}], "]"}]}]}], "Input",
 CellChangeTimes->{{3.722761331396912*^9, 
  3.722761368532557*^9}},ExpressionUUID->"177ecd18-83f9-4003-ba75-\
d0d2906a11dd"],

Cell[BoxData[
 RowBox[{"-", 
  FractionBox[
   RowBox[{
    RowBox[{"(", 
     RowBox[{"enl", "-", "epl"}], ")"}], " ", 
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "epl", "+", "erl"}], ")"}]}], 
   RowBox[{
    RowBox[{"-", "1"}], "+", "enl", "+", "epl", "+", "erl"}]]}]], "Output",
 CellChangeTimes->{
  3.722761378776958*^9},ExpressionUUID->"3f733a17-0a5c-4b89-a7aa-\
d1a08cc49e4a"],

Cell[BoxData[
 FractionBox[
  RowBox[{"enl", "-", "epl"}], 
  RowBox[{
   RowBox[{"-", "1"}], "+", "enl", "+", "erl"}]]], "Output",
 CellChangeTimes->{
  3.722761378785289*^9},ExpressionUUID->"a130c45e-e9e5-4be8-bd42-\
84d484a4e9e4"]
}, Open  ]]
}, Open  ]],

Cell[CellGroupData[{

Cell["Restate estimators in terms of p and \[CapitalDelta]", "Subsection",
 CellChangeTimes->{{3.722761525234252*^9, 
  3.7227615464317837`*^9}},ExpressionUUID->"1dc3059a-afae-426e-aa5d-\
3f9929b830ad"],

Cell[CellGroupData[{

Cell[BoxData[{
 RowBox[{"gammaE", " ", "=", " ", 
  RowBox[{"gamma", " ", "/.", " ", 
   RowBox[{"ep", "\[Rule]", 
    RowBox[{"p", "+", "\[CapitalDelta]"}]}]}]}], "\[IndentingNewLine]", 
 RowBox[{"gainE", " ", "=", " ", 
  RowBox[{"gain", " ", "/.", " ", 
   RowBox[{"ep", "\[Rule]", 
    RowBox[{"p", " ", "+", "\[CapitalDelta]"}]}]}]}]}], "Input",
 CellChangeTimes->{{3.722760872184292*^9, 
  3.7227609176763277`*^9}},ExpressionUUID->"f32b9096-4d3c-4d44-94d6-\
a3fa4525a831"],

Cell[BoxData[
 FractionBox[
  RowBox[{"epl", "+", 
   RowBox[{
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], ")"}], " ", 
    RowBox[{"(", 
     RowBox[{"p", "+", "\[CapitalDelta]"}], ")"}]}]}], 
  SuperscriptBox[
   RowBox[{"(", 
    RowBox[{
     RowBox[{"-", "1"}], "+", "p", "+", "\[CapitalDelta]"}], ")"}], 
   "2"]]], "Output",
 CellChangeTimes->{3.722760923072032*^9, 
  3.7227613788435593`*^9},ExpressionUUID->"002f04db-3d84-4d4c-a7d4-\
f0690667b67b"],

Cell[BoxData[
 FractionBox[
  RowBox[{"epl", "+", 
   RowBox[{
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], ")"}], " ", 
    RowBox[{"(", 
     RowBox[{"p", "+", "\[CapitalDelta]"}], ")"}]}]}], 
  RowBox[{
   RowBox[{"(", 
    RowBox[{
     RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], ")"}], " ", 
   RowBox[{"(", 
    RowBox[{
     RowBox[{"-", "1"}], "+", "p", "+", "\[CapitalDelta]"}], 
    ")"}]}]]], "Output",
 CellChangeTimes->{3.722760923072032*^9, 
  3.722761378857009*^9},ExpressionUUID->"9e420283-9ea3-4f5d-9c2c-\
c76d13cdcf45"]
}, Open  ]]
}, Open  ]],

Cell[CellGroupData[{

Cell["Calculate the elasticity of the two estimators", "Subsection",
 CellChangeTimes->{{3.722761566312463*^9, 
  3.7227615735585403`*^9}},ExpressionUUID->"164ee062-7e74-479b-9b1e-\
f5021a4cd241"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"ElasGain", " ", "=", " ", 
  RowBox[{"Simplify", "[", 
   RowBox[{
    RowBox[{"D", "[", 
     RowBox[{"gainE", ",", "\[CapitalDelta]"}], "]"}], 
    FractionBox["\[CapitalDelta]", "gainE"]}], "]"}]}]], "Input",
 CellChangeTimes->{{3.722760965806473*^9, 
  3.722761004029513*^9}},ExpressionUUID->"60d7c7d7-3ca4-4fd0-a90b-\
ee73930bf0b8"],

Cell[BoxData[
 RowBox[{"-", 
  FractionBox[
   RowBox[{
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "enl", "+", "epl", "+", "erl"}], ")"}], " ", 
    "\[CapitalDelta]"}], 
   RowBox[{
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "p", "+", "\[CapitalDelta]"}], ")"}], " ", 
    RowBox[{"(", 
     RowBox[{"epl", "+", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{
         RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], ")"}], " ", 
       RowBox[{"(", 
        RowBox[{"p", "+", "\[CapitalDelta]"}], ")"}]}]}], 
     ")"}]}]]}]], "Output",
 CellChangeTimes->{3.72276100449656*^9, 
  3.7227613789092083`*^9},ExpressionUUID->"6dc518f0-a6ee-4fc7-902a-\
9418d0d6c5e7"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"ElasGamma", " ", "=", " ", 
  RowBox[{"Simplify", "[", 
   RowBox[{
    RowBox[{"D", "[", 
     RowBox[{"gammaE", ",", "\[CapitalDelta]"}], "]"}], 
    FractionBox["\[CapitalDelta]", "gammaE"]}], "]"}]}]], "Input",
 CellChangeTimes->{{3.722761038787757*^9, 
  3.722761077217552*^9}},ExpressionUUID->"17e19618-b077-4c65-934c-\
c44baf114b89"],

Cell[BoxData[
 RowBox[{"-", 
  FractionBox[
   RowBox[{"\[CapitalDelta]", " ", 
    RowBox[{"(", 
     RowBox[{
      RowBox[{"2", " ", "epl"}], "+", 
      RowBox[{"enl", " ", 
       RowBox[{"(", 
        RowBox[{"1", "+", "p", "+", "\[CapitalDelta]"}], ")"}]}], "+", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{
         RowBox[{"-", "1"}], "+", "erl"}], ")"}], " ", 
       RowBox[{"(", 
        RowBox[{"1", "+", "p", "+", "\[CapitalDelta]"}], ")"}]}]}], ")"}]}], 
   RowBox[{
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "p", "+", "\[CapitalDelta]"}], ")"}], " ", 
    RowBox[{"(", 
     RowBox[{"epl", "+", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{
         RowBox[{"-", "1"}], "+", "enl", "+", "erl"}], ")"}], " ", 
       RowBox[{"(", 
        RowBox[{"p", "+", "\[CapitalDelta]"}], ")"}]}]}], 
     ")"}]}]]}]], "Output",
 CellChangeTimes->{3.7227610796681433`*^9, 
  3.722761378955555*^9},ExpressionUUID->"1cc27395-b6a4-4785-9234-\
74aeda05671c"]
}, Open  ]]
}, Open  ]],

Cell[CellGroupData[{

Cell["Calculate the ratio of the elasticities", "Subsection",
 CellChangeTimes->{{3.722761585967712*^9, 
  3.722761597465372*^9}},ExpressionUUID->"9704f14b-3e2d-47eb-94f4-\
694ffaa3568c"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"R", " ", "=", " ", 
  RowBox[{"FullSimplify", "[", 
   FractionBox["ElasGain", "ElasGamma"], "]"}]}]], "Input",
 CellChangeTimes->{{3.722761104344594*^9, 
  3.722761121848024*^9}},ExpressionUUID->"f128678a-7bc6-4dda-b398-\
c9538a09ab43"],

Cell[BoxData[
 FractionBox[
  RowBox[{
   RowBox[{"-", "1"}], "+", "enl", "+", "epl", "+", "erl"}], 
  RowBox[{
   RowBox[{"2", " ", "epl"}], "+", 
   RowBox[{"enl", " ", 
    RowBox[{"(", 
     RowBox[{"1", "+", "p", "+", "\[CapitalDelta]"}], ")"}]}], "+", 
   RowBox[{
    RowBox[{"(", 
     RowBox[{
      RowBox[{"-", "1"}], "+", "erl"}], ")"}], " ", 
    RowBox[{"(", 
     RowBox[{"1", "+", "p", "+", "\[CapitalDelta]"}], ")"}]}]}]]], "Output",
 CellChangeTimes->{3.722761122633512*^9, 
  3.7227613790052023`*^9},ExpressionUUID->"bf352934-f2f8-42c8-9228-\
844445890330"]
}, Open  ]]
}, Open  ]],

Cell[CellGroupData[{

Cell["Calculate the ratio of the elasticities given alpha = 0", "Subsection",
 CellChangeTimes->{{3.722761614478012*^9, 
  3.722761631083948*^9}},ExpressionUUID->"f74f5fe3-03e5-4b3f-92cf-\
4faea10d3f00"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"RA", " ", "=", " ", 
  RowBox[{"Simplify", "[", 
   RowBox[{
    RowBox[{"R", " ", "/.", " ", 
     RowBox[{
      RowBox[{"p", "+", "\[CapitalDelta]"}], "\[Rule]", " ", "ep"}]}], " ", "/.",
     " ", "nls"}], "]"}]}]], "Input",
 CellChangeTimes->{{3.722761219848729*^9, 3.722761235024622*^9}, {
  3.722761283678578*^9, 
  3.722761298182028*^9}},ExpressionUUID->"bdb0a8f5-ebfb-4cc9-a45d-\
86ed2c3586a3"],

Cell[BoxData[
 RowBox[{"-", 
  FractionBox[
   RowBox[{
    RowBox[{"-", "1"}], "+", "epl", "+", "erl"}], 
   RowBox[{"1", "+", "enl", "-", 
    RowBox[{"2", " ", "epl"}], "-", "erl"}]]}]], "Output",
 CellChangeTimes->{3.7227612986232977`*^9, 
  3.7227613790740347`*^9},ExpressionUUID->"0696a300-fca1-4d1c-aa73-\
125dbdfca725"]
}, Open  ]]
}, Open  ]]
},
WindowSize->{808, 701},
WindowMargins->{{Automatic, 211}, {18, Automatic}},
FrontEndVersion->"11.2 for Mac OS X x86 (32-bit, 64-bit Kernel) (September \
10, 2017)",
StyleDefinitions->"Default.nb"
]
(* End of Notebook Content *)

(* Internal cache information *)
(*CellTagsOutline
CellTagsIndex->{}
*)
(*CellTagsIndex
CellTagsIndex->{}
*)
(*NotebookFileOutline
Notebook[{
Cell[CellGroupData[{
Cell[1510, 35, 350, 7, 81, "Subsection",ExpressionUUID->"f2aa9cf8-4cfb-4b41-8681-a5a68cc52e2b"],
Cell[CellGroupData[{
Cell[1885, 46, 1585, 48, 178, "Input",ExpressionUUID->"d5918e45-489a-492c-a04c-e9d1b8ee1e68"],
Cell[3473, 96, 282, 7, 54, "Output",ExpressionUUID->"704f7289-3090-4724-82d9-d45c63aa0226"],
Cell[3758, 105, 452, 14, 55, "Output",ExpressionUUID->"b0501a5c-ad47-44ca-a219-7b8734897053"],
Cell[4213, 121, 452, 14, 55, "Output",ExpressionUUID->"42757dde-b5fb-4727-8c80-51cb15ae704c"],
Cell[4668, 137, 537, 17, 54, "Output",ExpressionUUID->"d95acf38-b1c1-4239-bf3f-8c09177aced0"]
}, Open  ]]
}, Open  ]],
Cell[CellGroupData[{
Cell[5254, 160, 259, 6, 81, "Subsection",ExpressionUUID->"00241716-2ee5-4097-bd88-2726d900d23d"],
Cell[CellGroupData[{
Cell[5538, 170, 313, 9, 30, "Input",ExpressionUUID->"012ea6d7-faf4-49f5-8619-7fcf63319552"],
Cell[5854, 181, 335, 9, 54, "Output",ExpressionUUID->"bf88be53-797b-4e78-95c3-7fe5f505d98c"]
}, Open  ]],
Cell[CellGroupData[{
Cell[6226, 195, 402, 9, 52, "Input",ExpressionUUID->"177ecd18-83f9-4003-ba75-d0d2906a11dd"],
Cell[6631, 206, 404, 13, 54, "Output",ExpressionUUID->"3f733a17-0a5c-4b89-a7aa-d1a08cc49e4a"],
Cell[7038, 221, 233, 7, 52, "Output",ExpressionUUID->"a130c45e-e9e5-4be8-bd42-84d484a4e9e4"]
}, Open  ]]
}, Open  ]],
Cell[CellGroupData[{
Cell[7320, 234, 202, 3, 54, "Subsection",ExpressionUUID->"1dc3059a-afae-426e-aa5d-3f9929b830ad"],
Cell[CellGroupData[{
Cell[7547, 241, 478, 11, 52, "Input",ExpressionUUID->"f32b9096-4d3c-4d44-94d6-a3fa4525a831"],
Cell[8028, 254, 497, 16, 55, "Output",ExpressionUUID->"002f04db-3d84-4d4c-a7d4-f0690667b67b"],
Cell[8528, 272, 579, 19, 54, "Output",ExpressionUUID->"9e420283-9ea3-4f5d-9c2c-c76d13cdcf45"]
}, Open  ]]
}, Open  ]],
Cell[CellGroupData[{
Cell[9156, 297, 196, 3, 54, "Subsection",ExpressionUUID->"164ee062-7e74-479b-9b1e-f5021a4cd241"],
Cell[CellGroupData[{
Cell[9377, 304, 361, 9, 49, "Input",ExpressionUUID->"60d7c7d7-3ca4-4fd0-a90b-ee73930bf0b8"],
Cell[9741, 315, 707, 23, 54, "Output",ExpressionUUID->"6dc518f0-a6ee-4fc7-902a-9418d0d6c5e7"]
}, Open  ]],
Cell[CellGroupData[{
Cell[10485, 343, 364, 9, 49, "Input",ExpressionUUID->"17e19618-b077-4c65-934c-c44baf114b89"],
Cell[10852, 354, 996, 31, 54, "Output",ExpressionUUID->"1cc27395-b6a4-4785-9234-74aeda05671c"]
}, Open  ]]
}, Open  ]],
Cell[CellGroupData[{
Cell[11897, 391, 187, 3, 54, "Subsection",ExpressionUUID->"9704f14b-3e2d-47eb-94f4-694ffaa3568c"],
Cell[CellGroupData[{
Cell[12109, 398, 261, 6, 49, "Input",ExpressionUUID->"f128678a-7bc6-4dda-b398-c9538a09ab43"],
Cell[12373, 406, 576, 17, 54, "Output",ExpressionUUID->"bf352934-f2f8-42c8-9228-844445890330"]
}, Open  ]]
}, Open  ]],
Cell[CellGroupData[{
Cell[12998, 429, 203, 3, 54, "Subsection",ExpressionUUID->"f74f5fe3-03e5-4b3f-92cf-4faea10d3f00"],
Cell[CellGroupData[{
Cell[13226, 436, 427, 11, 30, "Input",ExpressionUUID->"bdb0a8f5-ebfb-4cc9-a45d-86ed2c3586a3"],
Cell[13656, 449, 327, 9, 54, "Output",ExpressionUUID->"0696a300-fca1-4d1c-aa73-125dbdfca725"]
}, Open  ]]
}, Open  ]]
}
]
*)

(* End of internal cache information *)

(* NotebookSignature mv07H5hQVsZvDBKBqBOJw5b8 *)
