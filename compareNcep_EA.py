#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:11:35 2015

@author: jhchen
"""
import matplotlib
import numpy as np
import matplotlib.cm as cm
import datetime
from pylab import *
import matplotlib.pyplot as plt
import calendar
import string
import time 
year=2000
month=6
date1=datetime.datetime(year,month,1,0,0,0)
cdaystr=date1.strftime('%j')
cday=string.atoi(cdaystr)
nday=calendar.monthrange(year,month)[1]
its=(cday-1)*4
ite=its+nday*4
direra='D:/MyPaper/Phd01/Submitted/TEMP2/ERA/NEW/000101-001231/'
dirncep='D:/MyPaper/Phd01/Submitted/TEMP2/NCEP/000101-001231/'
#direra='Z:/DATA/LargeScale/NcepR2_Pre/'
#dirncep='Z:/DATA/LargeScale/NcepR2_Pre/000101-001231/'
pic_out='D:/MyPaper/Phd01/Submitted/TEMP2/'
nzera=37
nzncep=17
rgns=['PRD','MLYR','NEC','NPC']
nd=365
if calendar.isleap(year) :
    nd=366
nt=nd*4
det=datetime.timedelta(hours=6)
datestart=datetime.datetime(year,1,1,0,0,0)            
dateiso=[]            
for dt in range(0,nt):
    dateiso.append(datestart+dt*det)
xdate=[]
for tm in dateiso:
    xdate.append(datetime.datetime.strftime(tm,"%b/%d"))   
xdat=range(0,nt)
# read ncep
yearstr="%04d"%(year)
namencep=['Temp. Forcing(K/day)','Moisture Forcing (K/day)',  #0,1
          'Uwnd(m/s)',  'Vwnd (m/s)', 'Moisture (kg/kg)',    # 2,3,4
          'HGT (m)',  'Temp.(K)', 'Adjusted Omega(Pa/s)',   # 5,6,7
          'RH(%)',    'Theta(K)', 'Q1(K/day)',              #8,9,10
          'Q2(K/day)','HADQ(K/day)',' VADQ(K/day)',       # 11,12,13
          'TCHQ(K/day)', 'HADT(K/day)', 'VADT(K/day)',    # 14 15,16
          'TCHT(K/day)', 'Original Omega(Pa/s)']          #17，18
ncepdata=np.ndarray(shape=(nzncep,nt,19,4),dtype=float)
for ig in range(0,4):
    filename=yearstr+rgns[ig]+'_RAW.txt'
    filepath=dirncep+filename
    f=open(filepath)
    ff=f.readlines()[1:]
    onedim=[]
    linesplit=[]
    for line in ff:
        line=string.lstrip(line)
        tmpstr=line[:-1].split(':') #先把一行分成两个字符串，后面那个是需要的
        linesplit.append(tmpstr[1].split(' '))
    for lnstrs in linesplit:
        for strs in lnstrs:
            if strs!='':
                onedim.append(string.atof(strs))
    for it in range(0,nt):
        for k in range(0,nzncep):
            for iv in range(0,19):  # why is 19 not 18, because the first number is time index
                itkv=it*nzncep*20+k*20+iv+1
                scale=1.0
#                if iv==7:
#                    scale=100.
                ncepdata[k,it,iv,ig]=onedim[itkv]*scale
    del onedim,linesplit   
#
### plotting 
levs1=[-12,-9,-6,-3,3,6,9,12]
levcol1=['g','g','g','g','r','r','r','r']
linetype1=['dotted','dotted','dotted','dotted','solid','solid','solid','solid']
levs2=[-6,-3,-1,1,3,6]
levcol2=['g','g','g','r','r','r']
linetype2=['dotted','dotted','dotted','solid','solid','solid']
namels=['Q1','Q2']
monstr="%02d"%(month)
pncep=[1000, 925, 850, 700, 600, 500, 400, 300, 250, 
       200, 150, 100, 70, 50, 30, 20, 10]
pera=[1000, 975, 950,	925, 900, 875, 850, 825, 800, 775, 750, 700,
      650, 600, 550, 500, 450, 400, 350, 300, 250, 225, 200, 175,
      150, 125, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]
for ig in range(0,4):
    ivnp1=10
    ivnp2=11
    fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(15,4*2))
    axes[0]=plt.subplot(2,1,1)                         
    axes[0]=plt.contour(xdat[its:ite],pncep,ncepdata[:,its:ite,ivnp1,ig],colors=levcol1,
        linewidths=1,levels=levs1,linestyles=linetype1)
#    axes[0]=plt.contour(xdat[its:ite],pera,eradata[:,its:ite,ivec,ig])    
#    axes[0]=plt.contour(xdat[its:ite],pncep,ncepdata[:,its:ite,7,ig])                       
    plt.title(namencep[ivnp1]+' of NCEP '+yearstr+monstr,fontsize=16) 
#    plt.title('Adjusted Omega'+yearstr+monstr,fontsize=16)                         
    plt.axis([its, ite, 1000, 50])
    plt.clabel(axes[0],inline=1,fmt='%1.3f',fontsize=12) 
    plt.show()                        
    axx=fig.add_subplot(2,1,1)                         
    axx.set_xticks(range(its,ite,16))
    xticklabels = [xdate[nn] for nn in range(its,ite,16)] 
    axx.set_xticklabels(xticklabels, size=16)
    plt.ylabel('Pressure (hPa)')
#
    axes[1]=plt.subplot(2,1,2)                         
    axes[1]=plt.contour(xdat[its:ite],pncep,ncepdata[:,its:ite,ivnp2,ig],colors=levcol2,
        linewidths=1,levels=levs2,linestyles=linetype2)
#    axes[1]=plt.contour(xdat[its:ite],pncep,ncepdata[:,its:ite,ivnp2,ig])                             
    plt.title(namencep[ivnp2]+' of NCEP '+yearstr+monstr,fontsize=16)  
#    plt.title('Original Omega'+yearstr+monstr,fontsize=16)                        
    plt.axis([its, ite, 1000, 50])
    plt.clabel(axes[1],inline=1,fmt='%1.3f',fontsize=12) 
    plt.show()                        
    axx=fig.add_subplot(2,1,2)                         
    axx.set_xticks(range(its,ite,16))
    xticklabels = [xdate[nn] for nn in range(its,ite,16)] 
    axx.set_xticklabels(xticklabels, size=16)
    plt.ylabel('Pressure (hPa)')
    plt.show()
    strings=namencep[ivnp2].split('(') 
    strnm=strings[0].strip() # 去除左右边的空格                   
    plt.savefig(pic_out+rgns[ig]+yearstr+monstr+strnm+'.pdf')          
    plt.show()
    plt.close()
#"   xyz   ".strip()            # returns "xyz"  
#"   xyz   ".lstrip()           # returns "xyz   "  
#"   xyz   ".rstrip()           # returns "   xyz"  
#"  x y z  ".replace(' ', '')   # returns "xyz"  











                