# -*- coding: utf-8 -*-
"""
Created on Sun Mar 01 16:34:50 2015

@author: jhchen
"""
from netCDF4 import Dataset
import numpy as np
"""
dirin='X:/Data/ERA_interim/X2.5/'
fname='1979_sh_00.nc'
fpath=dirin+fname
f=Dataset(fpath,'a')
#for dims in f.dimensions.values():
#    print dims       # this is a test to check the dimensions in the file
lon=f.variables['longitude'][:]   # read 
lat=f.variables['latitude'][:]
lev=f.variables['level'][:]
fpath='X:/Data/NCEP/air.mon.mean.nc'
f2=Dataset(fpath,'a')
for dims in f.variables:
    print dims       # this is a test to check the dimensions in the file
lon2=f2.variables['lon'][:]   # read 
lat2=f2.variables['lat'][:]
lev2=f2.variables['level'][:]
fpath='X:/Data/ERA_interim/SRFX2.5/surface_LHSH_monthlymeans.nc'
f3=Dataset(fpath,'a')
for dims in f3.dimensions.values():
    print dims       # this is a test to check the dimensions in the file
lon3=f3.variables['longitude'][:]   # read 
lat3=f3.variables['latitude'][:]
#lev3=f3.variables['level'][:]
time=f3.variables['time'][:]
cc=f3.variables['slhf'][:]
"""
imm=0
tmp=0.
imt=0
for im in range(0,8,2):
    imm+=1
    tmp=tmp+1
    imt=imt+1
    print imm,tmp,imt
print tmp ,imt 
dirin='D:/Data/'
fpath=dirin+'test.txt'
fout=open(fpath,'w')
a=np.ndarray(shape=(5,10),dtype=float)


