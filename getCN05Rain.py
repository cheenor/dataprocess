#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:04:24 2015

@author: jhchen
"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import string
import calendar

dirin="Z:/DATA/CN05/CN05.2/"
prename="2400_CN5.2_Pre.nc"
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
slon.append(75.) ;  elon.append(92.5)
slat.append(27.5)  ;  elat.append(37.5)
#-----ETP----------
rgnm.append('ETP')
slon.append(87.5) ;  elon.append(107.5)
slat.append(27.5)  ;  elat.append(37.5)
#
nr=len(rgnm)
mondays=[31,28,31,30,31,30,31,31,30,31,30,31]
fpath=prename
pre=Dataset(fpath,'a')
lon=pre.variables['lon'][:]
lat=pre.variables['lat'][:]
time=pre.variables['time'][:]
rain=pre.variables['pre'][:]
fout=open('CN5.2_summer_rain.txt','w')
itme="%s "%"Year"
fout.write(itme)
for ir in range(0,nr):
	itme="%s "%rgnm[ir]
	fout.write(itme)
fout.write('\n')
idss=0
nx=len(lon)
ny=len(lat)
for iy in range(1961,2011):
	itme="%d "%iy
	fout.write(itme)
    idss=0
    mdd=0
    if calendar.isleap(iy):
        mondays[1]=29
    for m in range(0,6):
        mdd=mdd+mondays[m]
    for i in range(0,iy):
       ndd=365
        if calendar.isleap(iy):
           ndd=366
        idss=idss+ndd
    idss=idss+mdd
    for ir in range(0,nr):
        for it in range(idss,idss+92):
            tmp=0.0
            cont=0.
            for ix in range(0,nx):
                if lon[ix]>(slon[ir]) and lon[ix]<(elon[ir]):
                    for iy in range(0,ny):
                        if lat[iy]>slat[ir] and lat[iy]<elat[ir]:
                               if rain[it,iy,ix] >0. :
                                   tmp=tmp+rain[it,iy,ix]
                                   cont=cont+1.
        tmp=tmp/92./cont
        itme="%f "%tmp
		fout.write(itme)
	fout.write('\n')