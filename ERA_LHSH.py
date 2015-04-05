#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 23:08:52 2015

@author: jhchen
"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt


#...........setting---------------
dirin='X:/Data/ERA_interim/SRFX2.5/'
dirout='D:/MyPaper/Phd01/Submitted/RV01/data/'
fname='surface_LHSH_monthlymeans.nc'
datname='ERA_interim'
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
#---------------
rgnm.append('Test')
slon.append(75.) ;  elon.append(107.5)
slat.append(25-2.5)  ;  elat.append(40+2.5)
#
fhours=[3,6,9,12,3,6,9,12]
fpath=dirin+fname
sflux=Dataset(fpath,'a')
lon=sflux.variables['longitude'][:]   # read 
lat=sflux.variables['latitude'][:]
time=sflux.variables['time'][:]
nt=len(time)
ny=len(lat)
nx=len(lon)
nm=nt/8
del time 
sho=sflux.variables['sshf'][:]  # timexnlatxnlon
sho_units = sflux.variables['sshf'].units
sho_scale = sflux.variables['sshf'].scale_factor
sho_offset = sflux.variables['sshf'].add_offset
lho=sflux.variables['slhf'][:]  # timexnlatxnlon
sho_mon=np.ndarray(shape=(ny,nx,nm),dtype=float)
lho_mon=np.ndarray(shape=(ny,nx,nm),dtype=float)
for ix in range(0,nx):
    for iy in range(0,ny):
        im=0
        for i in range(0,nt-8,8):
            tmp1=0.0
            tmp2=0.0
            for j in range(0,8):
                ij=im*8+j
                tscale=fhours[j]*3600.
                tmp1=tmp1+sho[ij,iy,ix]/tscale
                tmp2=tmp2+lho[ij,iy,ix]/tscale
#                tscale=3*3600.
#                if j==0 or j==3:
#                    tmp1=tmp1+sho[ij,iy,ix]/tscale
#                    tmp2=tmp2+lho[ij,iy,ix]/tscale
#                else:
#                    tmp1=tmp1+(sho[ij,iy,ix]-sho[ij-1,iy,ix])/tscale
#                    tmp2=tmp2+(lho[ij,iy,ix]-lho[ij-1,iy,ix])/tscale                   
            sho_mon[iy,ix,im]=tmp1/8.
            lho_mon[iy,ix,im]=tmp2/8.
            im+=1
sho_sea=np.ndarray(shape=(ny,nx,nm/3),dtype=float)
lho_sea=np.ndarray(shape=(ny,nx,nm/3),dtype=float)
for ix in range(0,nx):
    for iy in range(0,ny):
        tmp1=sho_mon[iy,ix,0]+sho_mon[iy,ix,1]
        tmp2=lho_mon[iy,ix,0]+lho_mon[iy,ix,1]
        sho_sea[iy,ix,0]=tmp1/2.
        lho_sea[iy,ix,0]=tmp2/2.   ### first season DJF, just JF of the first year
        im=1
        for i in range(2,nm-3,3):       # season MAM,JJA,SON,/next year DJF
            tmp1=0.0
            tmp2=0.0
            for j in range(0,3):
                ij=(im-1)*3+j+2
                tmp1=tmp1+sho_mon[iy,ix,ij]
                tmp2=tmp2+lho_mon[iy,ix,ij]
            sho_sea[iy,ix,im]=tmp1/3.
            lho_sea[iy,ix,im]=tmp2/3.
            im+=1
ns=nm/3
nyr=ns/4            
sho_sea2=np.ndarray(shape=(ny,nx,4,nyr),dtype=float)
lho_sea2=np.ndarray(shape=(ny,nx,4,nyr),dtype=float)
for ix in range(0,nx):
    for iy in range(0,ny):
        for iyr in range(0,nyr):
            for ise in range(0,4):
                ij=iyr*4+ise
                sho_sea2[iy,ix,ise,iyr]=sho_sea[iy,ix,ij]
                lho_sea2[iy,ix,ise,iyr]=lho_sea[iy,ix,ij]
nvar=len(rgnm)
for iv in range(0,nvar):
    fpath=dirout+rgnm[iv]+datname+"_lhsh_1979-2014.txt"
    f=open(fpath,'w')
    itme="%s "%'Year'
    f.write(itme)
    itme="%s "%'DJF_SH'
    f.write(itme)
    itme="%s "%'DJF_LH'
    f.write(itme)
    itme="%s "%'MAM_SH'
    f.write(itme)
    itme="%s "%'MAM_LH'
    f.write(itme)
    itme="%s "%'JJA_SH'
    f.write(itme)
    itme="%s "%'JJA_LH'
    f.write(itme)
    itme="%s "%'SON_SH'
    f.write(itme)
    itme="%s "%'SON_LH'
    f.write(itme)    
    f.write('\n')
    for iyr in range(0,nyr):
        year="%d "%(iyr+1979)
        f.write(year)
        for ise in range(0,4):
            tmp1=0.0
            tmp2=0.0
            itmp=0.
            for ix in range(0,nx):
                if lon[ix]>(slon[iv]+2.5) and lon[ix]<(elon[iv]-2.5):
                    for iy in range(0,ny):
                        if lat[iy]>slat[iv] and lat[iy]<elat[iv]:
                            tmp1=tmp1+sho_sea2[iy,ix,ise,iyr]
                            tmp2=tmp2+lho_sea2[iy,ix,ise,iyr]
                            itmp+=1.
            seash="%f "%(-tmp1/itmp)
            sealh="%f "%(-tmp2/itmp)
            f.write(seash)
            f.write(sealh)
        f.write('\n')
    f.close()