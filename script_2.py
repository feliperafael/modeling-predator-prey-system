#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:16:53 2018

@author: Felipe Rafael de Souza
"""
import matplotlib.pyplot as plt
import numpy as np

owls_init   = [150, 150, 100, 10, 10]
mouses_init = [200, 300, 200, 20, 100]

owls_coef   = [0.7]
owls_coef_b   = np.linspace(0.001,0.006,20)
mouses_coef = [1.2]
owls_coef_b   = np.linspace(0.001,0.005,20)

times = 100

#@return new amount of owls 
def owl(a_coef, b_coef, owls_now, mouses_now):
    return (a_coef*owls_now + b_coef*mouses_now*owls_now)
#@return new amount of mouses    
def mouse(a_coef, b_coef, mouses_now, owls_now, time):
    if time % 10 == 0:
        return (a_coef*mouses_now - b_coef*mouses_now*owls_now - mouses_now*0.5)
    else:
        return (a_coef*mouses_now - b_coef*mouses_now*owls_now)

def plot(owls,mouses,owl_coef, mouse_coef):    
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
    plt.title("owls_coef: "+str(owl_coef)+" mouses_coef: "+str(mouse_coef))
    plt.legend(handles=[line_1, line_2])
    plt.axhline(y=0, linewidth=1, color='g')
    plt.axis([0, 100, 0, 1800])
    
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.15, right=0.95, hspace=0.30,
                    wspace=0.35)
    plt.show()
    
def extinction_check(population):
    for i in population:
        if i <= 1:
            return True
    return False

for scenario in range(len(owls_init)):
    for owl_coef in owls_coef:
        for mouse_coef in mouses_coef:
            for owl_coef_b in owls_coef_b:
                for mouse_coef_b in owls_coef_b:
            
                    #parameters
                    print("owl_coef : ",owl_coef)
                    print("owl_coef_b : ",owl_coef_b)
                    print("mouse_coef : ",mouse_coef)
                    print("mouse_coef_b : ",mouse_coef_b)
                    print("owls_init : ", owls_init[scenario])
                    print("mouses_init : ", mouses_init[scenario])
                    owls   = [owls_init[scenario]]
                    mouses = [mouses_init[scenario]]
                    
                    for time in range(times):
                        owls.append( owl(owl_coef, owl_coef_b, owls[time], mouses[time]) )
                        mouses.append( mouse(mouse_coef, mouse_coef_b, mouses[time], owls[time], time) )
                    if(extinction_check(owls) or extinction_check(mouses)):
                        print("THE POPULATION WAS EXTENDED")
                    else:
                        print("SURVIVED")
                        plot(owls,mouses,owl_coef, mouse_coef)

