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
from matplotlib.dates import DateFormatter
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
matplotlib.rcParams['savefig.dpi'] = 100
#####
ylevs=[1000, 925, 850, 700, 600, 500, 400, 300, 250, 
       200, 150, 100, 70, 50, 30, 20, 10]
lels=np.ndarray(shape=(19,8), dtype=float)  # set for contour levels of diff vars
lels[0,:]=[-8,-6,-4,-2,2,4,6,8]
lels[1,:]=[-8,-6,-4,-2,2,4,6,8]
lels[2,:]=[-15,-10,-5,5,10,15,20,25]
lels[3,:]=[-8,-6,-4,-2,2,4,6,8]
lels[4,:]=[0.003,0.006,0.009,0.012,0.015,0.018,0.021,0.024]
lels[5,:]=[100,300,500,700,900,1200,1500,2000]
lels[6,:]=[210,225,240,250,260,270,280,290]
lels[7,:]=[-0.2,-0.15,-0.1,-0.05,0.05,0.1,0.15,0.2]
lels[8,:]=[10,20,30,40,50,60,70,80]
lels[9,:]=[290,300,310,320,330,340,360,400]
lels[10,:]=[-8,-6,-4,-2,2,4,6,8]
lels[11,:]=[-8,-6,-4,-2,2,4,6,8]
lels[12,:]=lels[1,:]/4
lels[13,:]=lels[1,:]/2
lels[14,:]=lels[1,:]/2
lels[15,:]=lels[1,:]/4
lels[16,:]=lels[1,:]/2
lels[17,:]=lels[1,:]/2
lels[18,:]=[-0.2,-0.15,-0.1,-0.05,0.05,0.1,0.15,0.2]
#
f=open(datapath+'date_and_name.txt')
ff=f.readlines()
tmp1=[]
tmp2=[]
tmd=[]
tmlab=[]
for line in ff:
    tmp1.append(line[1:-1].split(' '))
for tss in tmp1[1:]:
    tmp2.append(tss[0]+' '+tss[1])
for strs in tmp2:
    tmd.append(time.strptime(strs,"%Y-%m-%d %H:%M"))
del tmp1,tmp2
f.close()
xdat=range(0,368)
for tm in tmd:
    tmlab.append(time.strftime("%m/%d", tm))
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
        fig=plt.figure(figsize=(20,4))
        CS=plt.contour(xdat,ylevs,zdat,levels=lels[m,:])
        plt.clabel(CS,inline=1,fontsize=12)
        plt.axis([0, 368, 1000, 10])
        plt.title(nms[m])
        axes=fig.add_subplot(111) 
        axes.set_xticks(range(0,368,20))
        xticklabels = [tmlab[nn] for nn in range(0,368,20)]      
        axes.set_xticklabels(xticklabels, size=10)
#        axes.xaixis_date(DateFormatter('%m-%d') )
        plt.savefig(outpic+nm+nms[m]+'.png')
        plt.show()
        plt.close()
        del zdat

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


