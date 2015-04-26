#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 02 15:06:04 2015

@author: jhchen
"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import string
import calendar
#...........setting---------------
dirin='D:/Data/ERA_Interim_LHSH/'
dirrain='X:/Data/ERA_interim/Rain/'
dirout=dirin #'D:/MyPaper/Phd01/Submitted/RV01/data/'
fname='surface_LHSH_monthlymeans.nc'
datname='ERA_interim'
year=range(1979,2015,2)
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
ngns=len(rgnm)
fhours=[3,6,9,12,3,6,9,12]
for iyear1 in year:
    iyear2=iyear1+1
    yearstr1="%04d"%(iyear1)
    yearstr2="%04d"%(iyear2)
    fpath=dirin+yearstr1+'-'+yearstr2+'.nc'
    sflux=Dataset(fpath,'a')
    lon=sflux.variables['longitude'][:]   # read 
    lat=sflux.variables['latitude'][:]
    time=sflux.variables['time'][:]
    nt=len(time)
    ny=len(lat)
    nx=len(lon)
    nm=nt/8
    del time 
    nt1=365*8
    nt2=365*8
    if calendar.isleap(iyear1):
        nt1=366*8
    if calendar.isleap(iyear2) :
        nt2=366*8    
    sho=sflux.variables['sshf'][:]  # timexnlatxnlon
    sho_units = sflux.variables['sshf'].units
    sho_scale = sflux.variables['sshf'].scale_factor
    sho_offset = sflux.variables['sshf'].add_offset
    lho=sflux.variables['slhf'][:]  # timexnlatxnlon
#
    fpath=dirrain+yearstr1+'-'+yearstr2+'_rain.nc'
    sflux=Dataset(fpath,'a')
    lon_r=sflux.variables['longitude'][:]   # read 
    lat_r=sflux.variables['latitude'][:]
    time_r=sflux.variables['time'][:]
    ntr=len(time_r)
    nyr=len(lat_r)
    nxr=len(lon_r)
    del time_r 
    nt1=365*8
    nt2=365*8
    if calendar.isleap(iyear1):
        nt1=366*8
    if calendar.isleap(iyear2) :
        nt2=366*8    
    tp=sflux.variables['tp'][:]  # timexnlatxnlon
    cp=sflux.variables['cp'][:]  # timexnlatxnlon
    cp_units = sflux.variables['cp'].units
    tp_units = sflux.variables['tp'].units 
    for ir in range(0,ngns):
        for i in range(0,2):
            if i==0:
                yearstr=yearstr1
                its=0
                ite=nt1
            else:
                yearstr=yearstr2
                its=nt1
                ite=nt1+nt2 
            fpath=dirout+rgnm[ir]+yearstr+"_lhsh_rain.txt"
            fout=open(fpath,'w')
            itme="%s "%'Timestep'
            fout.write(itme)
            itme="%s "%('SH'+'(W m-2)')
            fout.write(itme)
            itme="%s "%('LH'+'(W m-2)')
            fout.write(itme)
            itme="%s "%('Total prep'+'(mm hr)')
            fout.write(itme)
            itme="%s "%('conv. prep'+'(mm hr-1)')
            fout.write(itme)
            fout.write('\n')
            itt=0
            nty=nt2
            for it in range(its,ite):
                j=itt%8
                tmp1=0.0
                tmp2=0.0
                cont=0.0
                avg=0.0
                for ix in range(0,nx):
                    if lon[ix]>(slon[ir]+2.5) and lon[ix]<(elon[ir]-2.5):
                        for iy in range(0,ny):
                            if lat[iy]>slat[ir] and lat[iy]<elat[ir]:
#                                tscale=-fhours[j]*3600.
                                tscale=-3*3600
#                                tmp1=tmp1+sho[it,iy,ix]/tscale
#                                tmp2=tmp2+lho[it,iy,ix]/tscale
#                                cont+=1
                                if j==0 or j==4:
                                    tmp1=tmp1+sho[it,iy,ix]/tscale    #convert unit
                                    tmp2=tmp2+lho[it,iy,ix]/tscale
                                    cont+=1 
                                else:
                                    tmp1=tmp1+(sho[it,iy,ix]-sho[it-1,iy,ix])/tscale    #convert unit
                                    tmp2=tmp2+(lho[it,iy,ix]-lho[it-1,iy,ix])/tscale
                                    cont+=1
                tmp1=tmp1/cont
                tmp2=tmp2/cont
                itme="%d "%(itt+1)
                fout.write(itme)
                itme="%f "%(tmp1)
                fout.write(itme)
                itme="%f "%(tmp2)
                fout.write(itme)
#                              
# -----------------------------------------------------------------------------                                
#                j=itt%8
                tmp1=0.0
                tmp2=0.0
                cont=0.0
                avg=0.0
                for ix in range(0,nxr):
                    if lon_r[ix]>(slon[ir]+2.5) and lon_r[ix]<(elon[ir]-2.5):
                        for iy in range(0,nyr):
                            if lat_r[iy]>slat[ir] and lat_r[iy]<elat[ir]:
                                if j==0 or j==4:
                                    tmp1=tmp1+tp[it,iy,ix]*1000./3.    #convert m to mm hr-1
                                    tmp2=tmp2+cp[it,iy,ix]*1000./3.
                                    cont+=1
                                else:
                                    tmp1=tmp1+(tp[it,iy,ix]-tp[it-1,iy,ix])*1000./3.    #convert m to mm hr-1
                                    tmp2=tmp2+(cp[it,iy,ix]-cp[it-1,iy,ix])*1000./3.
                                    cont+=1
#                                    if tp[it,iy,ix]-tp[it-1,iy,ix] <0 or cp[it,iy,ix]-cp[it-1,iy,ix] <0 :
#                                        print 'tmp1=',tmp1,'tmp2=',tmp2, it
                tmp1=tmp1/cont
                tmp2=tmp2/cont
                itme="%f "%(tmp1)
                fout.write(itme)
                itme="%f "%(tmp2)
                fout.write(itme)
                itt=itt+1
#
                fout.write('\n')                              
            fout.close()
    del lon,lat,sho,lho
#Check   using the monthly data checking
dirin='X:/Data/ERA_interim/SRFX2.5/'
fname='surface_LHSH_monthlymeans.nc'
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
#                ij=im*8+j
#                tscale=fhours[j]*3600.
#                tmp1=tmp1+sho[ij,iy,ix]/tscale
#                tmp2=tmp2+lho[ij,iy,ix]/tscale 
                ij=im*8+j
                if j==0 or j==4 :
                    tscale=3*3600.
                    tmp1=tmp1+sho[ij,iy,ix]/tscale
                    tmp2=tmp2+lho[ij,iy,ix]/tscale
                else:
                    tscale=3*3600.
                    tmp1=tmp1+(sho[ij,iy,ix]-sho[ij-1,iy,ix])/tscale
                    tmp2=tmp2+(lho[ij,iy,ix]-lho[ij-1,iy,ix])/tscale                 
            sho_mon[iy,ix,im]=tmp1/8.
            lho_mon[iy,ix,im]=tmp2/8.
            im+=1
sho_etp=np.ndarray(shape=(12),dtype=float)
lho_etp=np.ndarray(shape=(12),dtype=float)
for im in range(0,12):
    tmp1=0.
    tmp2=0.
    itmp=0
    iv=5
    for ix in range(0,nx):
        if lon[ix]>(slon[iv]+2.5) and lon[ix]<(elon[iv]-2.5):
            for iy in range(0,ny):
                if lat[iy]>slat[iv] and lat[iy]<elat[iv]:
                    tmp1=tmp1+sho_mon[iy,ix,im]
                    tmp2=tmp2+lho_mon[iy,ix,im]
                    itmp+=1.
    sho_etp[im]=-tmp1/itmp
    lho_etp[im]=-tmp2/itmp
fpath=dirout+"ETP1979_lhsh_2.txt"
f=open(fpath)
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
shlh=np.ndarray(shape=(2,365*8),dtype=float)
for i in range(0,365*8):
    k=i*3
    shlh[0,i]=onedim[k+1]
    shlh[1,i]=onedim[k+2]
sho_etp2=np.ndarray(shape=(12),dtype=float)
lho_etp2=np.ndarray(shape=(12),dtype=float)
for im in range(0,12):
    dnm=calendar.monthrange(1979,im+1)[1]  #calendar.monthrange(1997,7) #reture two index, sencond is the day number
    its=0
    if im >0 :
        for i in range(0,im):
            dnt=calendar.monthrange(1979,i+1)[1]
            its=its+dnt*8
    ite=its+dnm*8
    tmp1=0.0
    tmp2=0.0
    rtt=ite-its
    for it in range(its,ite):
        tmp1=tmp1+shlh[0,it]
        tmp2=tmp2+shlh[1,it]
#        print tmp1,tmp2,it
    sho_etp2[im]=tmp1/rtt
    lho_etp2[im]=tmp2/rtt
#

