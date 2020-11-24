#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 21:08:59 2018

@author: Kaina
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import random

M = 2**16 ##65536
a = 5.0 
a2 = 33
B = (2**11)-1 ## 2047
B2 = (2**7)-1


r = np.random.uniform(0,1,5000)
theta = np.random.uniform(0, 2*np.pi, 5000)


normalRandom=[]
for i in range(5000):
    cos = 2*math.sqrt(-np.log(r[i]))*math.cos(theta[i])
    sin = 2*math.sqrt(-np.log(r[i]))*math.sin(theta[i])
    normalRandom.append(cos)
    normalRandom.append(sin)

#print normalRandom

#y = math.exp(math.pow(-i, 2)/2)/math.sqrt(2*math.pi)
    
x = np.arange(-5.0, 5.0, 0.2)
y = np.exp((-x**2)/2)/math.sqrt(2*math.pi)
#plt.plot(x, y)

#plt.show()

def function():
    for i in range(-5, 5, 1):
        y = math.exp(math.pow(-i, 2)/2)/math.sqrt(2*math.pi)
    print y
    return y





hist, bins = np.histogram(normalRandom, bins=100)
plt.plot(x*1.5, y*850)
#hist, bins = np.histogram(points, bins=100)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()
    
