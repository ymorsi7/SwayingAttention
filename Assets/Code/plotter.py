# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:05:07 2021

@author: prana
"""

from matplotlib import pyplot as plt
import numpy as np

data = np.genfromtxt(".\Yusuf Data\Yusuf V2\yusufv2avg.csv", delimiter=",")
t = data[0:104,0]
t = (t - t[0])/1e3
ppg = data[0:248,1]

data = np.genfromtxt("Yusuf_eye_open.csv", delimiter=",")
t_2 = data[0:104,0]
t_2 = ((t - t[0])/1e3)*1000
ppg_2 = data[0:104,1]
plt.plot(t, ppg)
plt.plot(t_2, ppg_2)
plt.title("Eye Open versus Drowsy Eye-aspect-ratio Graph for Yusuf")
#plt.plot(t[peaks], norm[peaks], 'rx')
#plt.plot(t, [thresh]*len(norm), "b--")
plt.ylabel("Eye-Aspect-ratio")
plt.xlabel("Time(s)")
plt.show()