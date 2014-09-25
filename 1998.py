#!/usr/bin/env python
"""
ploting for 1998

"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import string
TP=['ETP','WTP']
EC=['PRD','MLYR','NPC','NEC']
nms=['T_Ls','Q_Ls','U','V','moisture','HGT','AIR','Adj_omega',
     'RH','Theta','Q1','Q2','HT_Q2','VT_2','TT_Q2','HT_Q1','VT_Q1',
     'TT_Q1','Ori_omega']
levnm=['_lowlevel.txt','_Middlelevel.txt','_Hightlevel.txt','_Abovelevel.txt',
       '_Tropsphere.txt','_AllLevels.txt']     
lbls=['_ori','_fn4days']
outpic='D:/MyPaper/Phd01/Pics/1998/'
datapath='D:/MyPaper/Phd01/data/1998/'
result=[]
tmp=[]
f=open('D:/MyPaper/Phd01/data/1998/ETP_Hightlevel_ori.txt')
ff=f.readlines()
for line in ff:
    result.append(line[1:].split(' '))
for sl in result[:]:
    for ss in sl[:]:
        if ss!='':
            tmp.append(string.atof(ss))     
dat=np.ndarray(shape=(368,19), dtype=float)
for l in range(0,368):
    for i in range(0,19):
#        print i
        ll=l*19+i  
        dat[l][i]=tmp[ll] 
del tmp,result
f.close()



       