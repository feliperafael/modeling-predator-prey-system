#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:16:53 2018

@author: Felipe Rafael de Souza
"""
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
    #plt.figure(figsize=(10,60))
    
    plt.subplot(221)
    plt.plot(owls,mouses,'r')
    plt.xlabel("owls")
    plt.ylabel("mouses")
    plt.title("owls X mouses")
    #plt.show()
    
    plt.subplot(222)
    plt.plot(owls,'r')
    plt.ylabel("owls")
    #plt.show()
    plt.subplot(223)
    plt.plot(mouses,'r')
    plt.ylabel("mouses")
    
    plt.subplots_adjust(top=1.2, bottom=0.08, left=0.15, right=0.95, hspace=0.30,
                    wspace=0.35)
    plt.show()
    