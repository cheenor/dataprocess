#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:45:24 2015

@author: jhchen
"""
from netCDF4 import Dataset
import numpy as np
import os
#import matplotlib.pyplot as plt
#import string
#import calendar
dataname="3B43"
dirin="E:/Data/TRMM/"+dataname+"/"
dirout="D:/MyPaper/Phd01/Submitted/RV02/Data/"
iys,iye=1998,2013
nyr=iye-iys+1
rgnm=[]
slon=[]
elon=[]
slat=[]
elat=[]
#-----PRD----------
rgnm.append('PRD')
slon.append(107.5) ; elon.append(117.5)
slat.append(17.5)  ;  elat.append(27.5)
#-----MLYR----------
rgnm.append('MLYR')
slon.append(110.) ;  elon.append(120.)
slat.append(25.)  ;  elat.append(35.)
#-----NPC----------
rgnm.append('NPC')
slon.append(110.) ;  elon.append(120.)
slat.append(32.5)  ;  elat.append(42.5)
#-----NEC----------
rgnm.append('NEC')
slon.append(120.) ;  elon.append(130.)
slat.append(40.)  ;  elat.append(50.)
#-----WTP----------
rgnm.append('WTP')
slon.append(80.) ;  elon.append(90.)
slat.append(27.5)  ;  elat.append(37.5)
#-----ETP----------
rgnm.append('ETP')
slon.append(90) ;  elon.append(100)
slat.append(27.5)  ;  elat.append(37.5)
nr=len(rgnm)
#
pcp=np.ndarray(shape=(nr,nyr,12),dtype=float)
#
prename="3B43.19980101.7.nc"
fpath=dirin+prename
fnc=Dataset(fpath,'a')
lon=fnc.variables['longitude'][:]
lat=fnc.variables['latitude'][:]
time=fnc.variables['time'][:]
rain=fnc.variables['pcp'][:]
err=fnc.variables['err'][:]
weight=fnc.variables['weight'][:]
nx=len(lon)
nt=len(time)
ny=len(lat)
for a in fnc.variables:
    print a
fnc.close()
del rain,err,weight
for iyy in range(iys,iye+1):
    iyr=iyy-iys
    yearstr="%4.4d"%iyy
    for im in range(0,12):
        monstr="%2.2d"%(im+1)
        daystr="01"        
        prename=dataname+"."+yearstr+monstr+daystr+".7.nc"
        fpath=dirin+prename
        if os.path.exists(fpath):
            fpath=fpath
        else:
            prename=dataname+"."+yearstr+monstr+daystr+".7A.nc"
            fpath=dirin+prename
        fnc=Dataset(fpath,'a')
#        lon=fnc.variables['longitude'][:]
#        lat=fnc.variables['latitude'][:]
#        time=fnc.variables['time'][:]
        rain=fnc.variables['pcp'][:]
        for ir in range(0,nr):
            tmp=0.0
            cont=0.0
            for ix in range(0,nx):
                if lon[ix]>(slon[ir]) and lon[ix]<(elon[ir]):
                    for iy in range(0,ny):
                        if lat[iy]>slat[ir] and lat[iy]<elat[ir]:
                            if rain[0,iy,ix] >0. : # 0 is the subscript of time
                                tmp=tmp+rain[0,iy,ix]*24  # convert mm/hr to mm/day
                                cont=cont+1.
            pcp[ir,iyr,im]=tmp/cont
        fnc.close()
        del rain
#
fpath=dirout+"TRMM_"+dataname+"_summerrain.txt"
fpre=open(fpath,'w')
fpath=dirout+"TRMM_"+dataname+"_summerrain_ano.txt"
fpreao=open(fpath,'w')
#
itme="%s "%"Year"
fpre.write(itme)
fpreao.write(itme)
for ir in range(0,nr):
    itme="%s "%rgnm[ir]
    fpre.write(itme)
    fpreao.write(itme)
fpre.write('\n')
fpreao.write('\n')
#
pcpmean=np.ndarray(shape=(nr),dtype=float)
for ir in range(0,nr):
    tmp=0.
    cont=0.
    for iy in range(0,nyr):
        for im in range(5,8):
            tmp=tmp+pcp[ir,iy,im]
            cont=cont+1.
    pcpmean[ir]=tmp/cont
#
for iy in range(0,nyr):
    iyy=iy+iys
    itme="%d "%iyy
    fpre.write(itme)
    fpreao.write(itme)
    for ir in range(0,nr):
        tmp=0.0
        cont=0.0
        for im in range(5,8): # june, july and august
            tmp=tmp+pcp[ir,iy,im]
            cont=cont+1.
        itme="%f "%(tmp/cont)
        fpre.write(itme)
        itme="%f "%(tmp/cont-pcpmean[ir])
        fpreao.write(itme)
    fpre.write('\n')
    fpreao.write('\n')
fpre.close()
fpreao.close()                             
                
    