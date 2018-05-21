#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:16:53 2018

@author: Felipe Rafael de Souza
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

#@return new amount of owls 
def owl(owls_now, mouses_now):
    return (0.7*owls_now + 0.002*mouses_now*owls_now)
#@return new amount of mouses    
def mouse(mouses_now, owls_now):
    return (1.2*mouses_now - 0.001*mouses_now*owls_now)

owls_init   = [150,150,100,10]
mouses_init = [200,300,200,20]

times = 100

for scenario in range(len(owls_init)):
    owls   = [owls_init[scenario]]
    mouses = [mouses_init[scenario]]
    
    for time in range(times):
        owls.append( owl(owls[time], mouses[time]) )
        mouses.append( mouse(mouses[time], owls[time]) )
    
    plt.figure(1)
    plt.subplot(121)
    plt.plot(owls,mouses,'r')
    plt.xlabel("owls")
    plt.ylabel("mouses")
    plt.title("owls X mouses")
    
    plt.subplot(122)
    line_1, = plt.plot(owls,'r', label='owls')
    line_2, = plt.plot(mouses,'b', label='mouses')
    plt.ylabel("number of individuals in population")
    plt.xlabel("time")
    plt.legend(handles=[line_1, line_2])
    plt.axhline(y=0, linewidth=1, color='g')
    plt.axis([0, 100, 0, 1800])
    
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.15, right=0.95, hspace=0.30,
                    wspace=0.35)
    plt.show()
    
