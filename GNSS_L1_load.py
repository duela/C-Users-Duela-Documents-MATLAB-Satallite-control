# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:42:00 2019

@author: Darius
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.io


#%% load mat file
Tx=1.01 # h analysis time (birthday Tx=M.dd   ???)

FN='VDU_201006.mat'
A={}
scipy.io.loadmat(FN, A)

print("Data loaded")

X = A['X']
Y = A['Y']
Z = A['Z']

fL1=1575.42 #MHz (10.23 MHz × 154)
df0=720# Hz, daznio nuokrypis del ZQ?
ppm=1E6*df0/(fL1*1E6)
Y=Y-df0

Vr=Y/(fL1*1E6)*3E8 # relative speed to receiver



#%% plot 2d image

ZZ=10*np.log10(Z); Min_Z=0+np.min(ZZ[0:1000,:]); Max_Z=-0+np.max(ZZ[0:1000,:])

fig = plt.figure(10)
plt.clf()
plt.pcolormesh(X/3600,Vr,ZZ.T, cmap=cm.jet, shading ='gouraud', vmin=Min_Z, vmax=Max_Z)
plt.axis('on')
plt.xlabel('t, h'), plt.ylabel(r'Vr, m/s')

#plt.show()

fig = plt.figure(11)
plt.clf()
plt.pcolormesh(X/3600,Y,ZZ.T, cmap=cm.jet, shading ='gouraud', vmin=Min_Z, vmax=Max_Z)
plt.axis('on')

plt.xlabel('t, h'), plt.ylabel(r'$\Delta$F, Hz')


plt.show()

#%% plot data @ Tx

II=np.where(X[0]/3600>=Tx)
II=II[0][0]
dF=Y[:,1]
Vr=dF/(fL1*1E6)*3E8 # relative speed to receiver

An=Z[II,:];

plt.figure(21)
plt.clf()
plt.plot(dF,An)

plt.xlabel(r'$\Delta$F, Hz'), plt.ylabel('Anorm')
plt.xlim(-8000, 8000)

plt.figure(22)
plt.clf()
plt.plot(Vr,An)

plt.xlabel(r'Vr, m/s'), plt.ylabel('Anorm')

plt.xlim(-1500, 1500)
plt.show()

#%%
An=An-min(An); An=An/max(An);
