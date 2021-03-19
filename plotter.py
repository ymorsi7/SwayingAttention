# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:05:07 2021

@author: prana
"""

from matplotlib import pyplot as plt
import numpy as np

data = np.genfromtxt("AustinAvg.csv", delimiter=",")
t = data[0:208,0]
t = (t - t[0])/1e3
ppg = data[0:208,1]

data = np.genfromtxt("austin-eyeopen.csv", delimiter=",")
t_2 = data[:,0]
t_2 = ((t - t[0])/1e3)*1000
ppg_2 = data[:,1]
plt.plot(t, ppg)
plt.plot(t_2, ppg_2)
#plt.title("Detected Peaks = %d" % count)
#plt.plot(t[peaks], norm[peaks], 'rx')
#plt.plot(t, [thresh]*len(norm), "b--")
plt.show()