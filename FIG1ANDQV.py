#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 05 12:40:54 2015

@author: jhchen
"""
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, cm
import numpy as np
import matplotlib.pyplot as plt
from numpy import meshgrid

ldlon=70.
ldlat=0.
rulon=160.
rulat=55.
dirin='D:/MyPaper/Phd01/data/'
dirout='D:/MyPaper/Phd01/Submitted/RV01/Pic/'
fpath=dirin+'GTOPO30_10MIN.CDF' #'LAND_10MIN.nc'
geo=Dataset(fpath,'a')
lon= geo.variables['lon'][:]   # read nort to south
tmstp=geo.variables['time'][:]
lat=geo.variables['lat'][:]
hgto=geo.variables['HT'][:]
hgt=hgto[0,:,:]
#----- figure 1 
fig = plt.figure(figsize=(8,8)) ### figure 8"X8"
ax = fig.add_axes([0.1,0.1,0.8,0.8])
#m=Basemap(width=12000000,height=9000000,projection='lcc', lat_1=10., lat_2=55.,
#          lat_0=33.,lon_0=130.,resolution='l')   ##### lat_l left_down corner  lat_2 left_up corner,lat_0 centre
m=Basemap(projection='lcc', llcrnrlon=ldlon,llcrnrlat=ldlat,urcrnrlon=rulon,urcrnrlat=rulat,
          lat_1=15.,lat_2=45.,lat_0=35.,lon_0=105.,rsphere=6371200., resolution='l')   ##### lat_l left_down corner  lat_2 left_up corner,lat_0 centre
m.drawcoastlines() #
m.drawcountries() #
# draw parallels.
parallels = np.arange(-90,90,10.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = np.arange(0.,360.,10.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) 
ny = hgt.shape[0]; nx = hgt.shape[1]
#lons, lats = m.makegrid(nx, ny) # get lat/lons of ny by nx evenly space grid.
lons=np.ndarray(shape=(ny,nx),dtype=float)
lats=np.ndarray(shape=(ny,nx),dtype=float)
for i in range(0,ny):
    for j in range(0,nx):
        lons[i,j]=lon[j]
        lats[i,j]=lat[i]
x, y = m(lons, lats) # compute map proj coordinates. 
#xx = linspace(0, map.urcrnrx, hgt.shape[1])
#yy = linspace(0, map.urcrnry, hgt.shape[0])
#x, y = meshgrid(xx, yy) 
# draw filled contours.
#clevs = [0,1,2.5,5,7.5,10,15,20,30,40,50,70,100,150,200,250,300,400,500,600,750]
clevs = [-50,0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500]
cs = m.contourf(x,y,hgt,clevs,cmap='binary')
# add colorbar.
cbar = m.colorbar(cs,location='bottom',pad="5%")
cbar.set_label('m')
# add title
#plt.title(prcpvar.long_name+' for period ending '+prcpvar.dateofdata)
plt.savefig(dirout+'Rv01_figure1.pdf')  
plt.show()