#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:25:17 2018

@author: Kaina
"""
import numpy as np
import matplotlib.pyplot as plt
import math

M = 2**16 ##65536
a = 5.0 
B = (2**11)-1 ## 2047

RNG = [0    ]

def Xnplus1(a, B, M):
    for i in range(M-1):
        Xi = RNG[i]
        #print Xi
        value = (a*Xi + B) % M
        RNG.append(value)
    return RNG

xValues = Xnplus1(a, B, M)

print len(xValues)

values=[]
for i in xValues:
    vals = 2*i/M-1
    values.append(vals)
    

    
DFT = np.fft.fft(values)
DFT_squared = []
for i in DFT:
    vals = abs(i**2)
    vals = (vals/M)
    DFT_squared.append(vals)

iDFT = np.fft.ifft(DFT_squared).real

print iDFT


#hist, bins = np.histogram(values, bins=100)
# =============================================================================
# xs = []
# for i in range(M):
#     xs.append(i)
#     
# =============================================================================
xs = np.arange(0, M)    
    
plt.plot(xs, iDFT,linestyle="",marker="o", markersize=3)
# =============================================================================
# hist, bins = np.histogram(iDFT, bins=100)
# width = 0.7 * (bins[1] - bins[0])
# center = (bins[:-1] + bins[1:]) / 2
# plt.bar(center, hist, align='center', width=width)
# =============================================================================
plt.show()




