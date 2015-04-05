#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:45:14 2015

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
#direra='D:/MyPaper/Phd01/Submitted/TEMP2/ERA/000101-001231/'
direra='X:/Data/ERA_interim/ERA_EA/000101-001231/'
dirncep='D:/MyPaper/Phd01/Submitted/TEMP2/NCEP/000101-001231/'
#direra='Z:/DATA/LargeScale/NcepR2_Pre/'
#dirncep='Z:/DATA/LargeScale/NcepR2_Pre/000101-001231/'
pic_out='D:/MyPaper/Phd01/Submitted/TEMP2/'
nzera=37
nzncep=17
rgns=['MLYR','NEC']
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
#
# read ERA forcing
nameera=['Temp. Forcing(K/day)','Moisture Forcing (K/day)',  #0,1
          'Uwnd(m/s)',  'Vwnd (m/s)', 'Moisture (kg/kg)',    # 2,3,4
          'HGT (m)',  'Temp.(K)', 'Adjusted Omega(Pa/s)',   #5,6,7
             'Theta(K)', 'Q1(K/day)',                       #8,9
          'Q2(K/day)','HADQ(K/day)',' VADQ(K/day)',         # 10,11,12
          'TCHQ(K/day)', 'HADT(K/day)', 'VADT(K/day)',     # 13,14,15
          'TCHT(K/day)', 'Original Omega(Pa/s)']           #16,17
ivec=9
yearstr="%04d"%(year)
eradata=np.ndarray(shape=(nzera,nt,18,2),dtype=float)
for ig in range(0,2):
    filename=yearstr+rgns[ig]+'_RAW.txt'
    filepath=direra+filename
    f=open(filepath)
    ff=f.readlines()[1:]
    onedim=[]
    linesplit=[]
    for line in ff:
        line=string.lstrip(line)
        linesplit.append(line[:-1].split(' '))
    for lnstrs in linesplit:
        for strs in lnstrs:
            if strs!='':
                onedim.append(string.atof(strs))
    for it in range(0,nt):
        for k in range(0,nzera):
            for iv in range(0,18):  # why is 19 not 18, because the first number is time index
                itkv=it*nzera*19+k*19+iv+1
                eradata[k,it,iv,ig]=onedim[itkv]
    del onedim,linesplit                
# read ncep
namencep=['Temp. Forcing(K/day)','Moisture Forcing (K/day)',  #0,1
          'Uwnd(m/s)',  'Vwnd (m/s)', 'Moisture (kg/kg)',    # 2,3,4
          'HGT (m)',  'Temp.(K)', 'Adjusted Omega(Pa/s)',   # 5,6,7
          'RH(%)',    'Theta(K)', 'Q1(K/day)',              #8,9,10
          'Q2(K/day)','HADQ(K/day)',' VADQ(K/day)',       # 11,12,13
          'TCHQ(K/day)', 'HADT(K/day)', 'VADT(K/day)',    # 14 15,16
          'TCHT(K/day)', 'Original Omega(Pa/s)']          #17，18
if ivec<8:
    ivnp=ivec
else:    
    ivnp=ivec+1
ncepdata=np.ndarray(shape=(nzncep,nt,19,2),dtype=float)
for ig in range(0,2):
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
levs1=[-9,-6,-3,-1,1,3,6,9]
levcol1=['g','g','g','g','r','r','r','r']
linetype1=['dotted','dotted','dotted','dotted','solid','solid','solid','solid']
levs2=[-9,-6,-3,-1,1,3,6,9]
levcol2=['g','g','g','g','r','r','r','r']
linetype2=['dotted','dotted','dotted','dotted','solid','solid','solid','solid']
namels=['Q1','Q2']
monstr="%02d"%(month)
pncep=[1000, 925, 850, 700, 600, 500, 400, 300, 250, 
       200, 150, 100, 70, 50, 30, 20, 10]
pera=[1000, 975, 950,	925, 900, 875, 850, 825, 800, 775, 750, 700,
      650, 600, 550, 500, 450, 400, 350, 300, 250, 225, 200, 175,
      150, 125, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]
for ig in range(0,2):
    fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(15,4*2))
    axes[0]=plt.subplot(2,1,1)
    if ivec in (0,1,9,10,11,12,13,14,15,16):                         
        axes[0]=plt.contour(xdat[its:ite],pera,eradata[:,its:ite,ivec,ig],colors=levcol1,
            linewidths=1,levels=levs1,linestyles=linetype1)
    else:
        axes[0]=plt.contour(xdat[its:ite],pera,eradata[:,its:ite,ivec,ig])    
#    axes[0]=plt.contour(xdat[its:ite],pncep,ncepdata[:,its:ite,7,ig])                       
    plt.title(nameera[ivec]+' of ERA_Interim '+yearstr+monstr,fontsize=16) 
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
    if ivec in (0,1,9,10,11,12,13,14,15,16):                           
        axes[1]=plt.contour(xdat[its:ite],pncep,ncepdata[:,its:ite,ivnp,ig],colors=levcol2,
            linewidths=1,levels=levs2,linestyles=linetype2)
    else:
        axes[1]=plt.contour(xdat[its:ite],pncep,ncepdata[:,its:ite,ivnp,ig])                             
    plt.title(namencep[ivnp]+' of NCEP '+yearstr+monstr,fontsize=16)  
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
    strings=namencep[ivnp].split('(') 
    strnm=strings[0].strip() # 去除左右边的空格                   
    plt.savefig(pic_out+rgns[ig]+yearstr+monstr+strnm+'.pdf')          
    plt.show()
    plt.close()
#"   xyz   ".strip()            # returns "xyz"  
#"   xyz   ".lstrip()           # returns "xyz   "  
#"   xyz   ".rstrip()           # returns "   xyz"  
#"  x y z  ".replace(' ', '')   # returns "xyz"  











                