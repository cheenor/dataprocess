#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:31:26 2015

@author: jhchen
"""
from netCDF4 import Dataset
import numpy as np
#import matplotlib.pyplot as plt
#import string
#import calendar

dirin="Z:/DATA/CN05/CN05.2/"
dirout="D:/MyPaper/Phd01/Submitted/RV02/Data/"
prename="CN5.2_Pre_Mon.nc"
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
#
nr=len(rgnm)
mondays=[31,28,31,30,31,30,31,31,30,31,30,31]
fpath=dirin+prename
pre=Dataset(fpath,'a')
lon=pre.variables['lon'][:]
lat=pre.variables['lat'][:]
time=pre.variables['time'][:]
rain=pre.variables['pre'][:]
fout=open(dirout+'CN5.2_summer_rain.txt','w')
itme="%s "%"Year"
fout.write(itme)
for ir in range(0,nr):
    itme="%s "%rgnm[ir]
    fout.write(itme)
fout.write('\n')
idss=0
nx=len(lon)
ny=len(lat)
nyy=2011-1961
summer=np.ndarray(shape=(nr,nyy), dtype=float)
for iyy in range(1961,2011):
    itme="%d "%iyy
    fout.write(itme)
    yskip=(iyy-1961)*12
    mskip=5
    idss=yskip+mskip
    for ir in range(0,nr):
        tmp=0.0
        cont=0.
        for it in range(idss,idss+3):     
            for ix in range(0,nx):
               if lon[ix]>(slon[ir]) and lon[ix]<(elon[ir]):
                   for iy in range(0,ny):
                       if lat[iy]>slat[ir] and lat[iy]<elat[ir]:
                           if rain[it,iy,ix]>0. :
                               tmp=tmp+rain[it,iy,ix]
                               cont=cont+1.
        tmp=tmp/cont
        summer[ir,iyy-1961]=tmp
        itme="%f "%tmp
        fout.write(itme)
    fout.write('\n')
fout.close()
del rain
nyr=nyy
pcpmean=np.ndarray(shape=(nr),dtype=float)
for ir in range(0,nr):
    tmp=0.
    cont=0.
    for iy in range(0,nyr):
        tmp=tmp+summer[ir,iy]
        cont=cont+1.
    pcpmean[ir]=tmp/cont
fout=open(dirout+'CN5.2_summer_rain_ano.txt','w')
itme="%s "%"Year"
fout.write(itme)
for ir in range(0,nr):
    itme="%s "%rgnm[ir]
    fout.write(itme)
fout.write('\n')
for iyr in range(0,nyr):
    itme="%d "%(iyr+1961)
    fout.write(itme)
    for ir in range(0,nr):
        itme="%f "%(summer[ir,iyr]-pcpmean[ir])
        fout.write(itme)
    fout.write('\n')
fout.close()