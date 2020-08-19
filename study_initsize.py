#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import module_initsize
import math


# In[6]:


mode_to_test = 'speaking' # enter 'speaking','coughing', or 'breathing'

T_range = [5.0,10,15,20,25,30,35]
RH_range = [10,20,30,40,50,60,70,80,90,100]

colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(T_range)))

for condT in range(len(T_range)): # Study the effect of varying temperature with fixed RH at 50% 
    T = T_range[condT]
    RH = 50
    if mode_to_test == 'speaking':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.speaking(T,RH)
    elif mode_to_test == 'coughing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.coughing(T,RH)
    elif mode_to_test == 'breathing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.breathing(T,RH)
    c = colors[condT]
    #p0 = [67,0.00093,-0.00035]
    popt, pcov = curve_fit(module_initsize.sknorm, t_settle, numcon)
    rsq = module_initsize.gfit(t_settle,numcon,popt)
    print(rsq)
    tspan = np.linspace(0,np.amax(t_settle,),50)
    numfitcurve = module_initsize.sknorm(tspan,popt[0],popt[1],popt[2])
    plt.scatter(t_settle, numcon, color=c, s=5, label=str(T))
    plt.plot(tspan, numfitcurve, color=c)
#label_list = [str(x) for x in T_range]
plt.axis([0, 100, 0, 1.2*np.amax(numcon)+20])
plt.title("Settling time distribution under varying T (with 50% RH)")
plt.xlabel('Settling time in hr')
plt.ylabel('Number concentration in cm^-3')
#plt.legend(label_list)
plt.legend(loc="lower right")
plt.show()

colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(RH_range)))

for condRH in range(len(RH_range)): # Study the effect of varying RH with fixed T at 25 C
    T = 25
    RH = RH_range[condRH]
    if mode_to_test == 'speaking':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.speaking(T,RH)
    elif mode_to_test == 'coughing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.coughing(T,RH)
    elif mode_to_test == 'breathing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.breathing(T,RH)
    c = colors[condRH]
    #p0 = [67,0.00093,-0.00035]
    popt, pcov = curve_fit(module_initsize.sknorm, t_settle, numcon)
    rsq = module_initsize.gfit(t_settle,numcon,popt)
    print(rsq)
    tspan = np.linspace(0,np.amax(t_settle),50)
    numfitcurve = module_initsize.sknorm(tspan,popt[0],popt[1],popt[2])
    plt.scatter(t_settle, numcon, color=c, s=5, label=str(RH))
    #plt.plot(t_settle,numcon)
    plt.plot(tspan, numfitcurve, color=c)
    
plt.axis([0, 100, 0, 1.2*np.amax(numcon)])
plt.title("Settling time distribution under varying RH (with T = 25 C)")
plt.xlabel('Settling time in hr')
plt.ylabel('Number concentration in cm^-3')
#plt.legend(label_list)
plt.legend(loc="upper right")
plt.show()

plt.title("Initial size distribution of droplets generated")
plt.scatter(sizeclass,numcon,s=10)
plt.xlabel('Initial size in um')
plt.ylabel('Number concentration in cm^-3')
plt.show()


# In[ ]:




