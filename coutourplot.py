#!/usr/bin/env python
"""
ploting for 1998

"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.dates as matdate
import string
import time 
rgns=['ETP','WTP','PRD','MLYR','NPC','NEC']
nms=['T_Ls','Q_Ls','U','V','moisture','HGT','AIR','Adj_omega',
     'RH','Theta','Q1','Q2','HT_Q2','VT_2','TT_Q2','HT_Q1','VT_Q1',
     'TT_Q1','Ori_omega']
outpic='D:/MyPaper/Phd01/Pics/1998/'
datapath='D:/MyPaper/Phd01/data/1998/'
### read the date
###  common setting for plotting
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['contour.negative_linestyle'] = 'dashed'
matplotlib.rcParams['savefig.dpi'] = 300
#####
ylevs=[1000, 925, 850, 700, 600, 500, 400, 300, 250, 
       200, 150, 100, 70, 50, 30, 20, 10]
f=open(datapath+'date_and_name.txt')
ff=f.readlines()
tmp1=[]
tmp2=[]
tmd=[]
for line in ff:
    tmp1.append(line[1:-1].split(' '))
for tss in tmp1[1:]:
    tmp2.append(tss[0]+' '+tss[1])
for strs in tmp2:
    tmd.append(time.strptime(strs,"%Y-%m-%d %H:%M"))
del tmp1,tmp2
f.close()
xdat=range(0,368)
#print tmd[1]
for nm in rgns:
    f=open(datapath+nm+'_raw_ori.txt')
    ff=f.readlines()
    tmp1=[]
    tmp2=[]   
    for line in ff:
        tmp1.append(line[1:-1].split(' '))
    for tss in tmp1:
        for ts in tss:
            if ts!='' :
                tmp2.append(string.atof(ts))
    dat=np.ndarray(shape=(17,368,19), dtype=float)
    x=dat[1,2,3]
    del tmp1
    ll=0
    f.close()
    for l in range(0,368):
        for k in range(0,17):
            for m in range(0,19):
                ll=l*17*19+k*19+m
                dat[k,l,m]=tmp2[ll]
#    del tmp2
######## plotting 
    for m in range(1,19):
        zdat=dat[:,:,m]
        plt.figure(figsize=(20,4))
        CS=plt.contour(xdat,ylevs,zdat,6)
        plt.clabel(CS,inline=1,fontsize=12)
        plt.axis([0, 368, 1000, 10])
        plt.title(nms[m])
        plt.savefig(outpic+nm+nms[m]+'.png')
        plt.show()
        plt.close()
        del zdat

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


