#!/usr/bin/env python
# coding: utf-8

# In[74]:


import csv
import numpy as np
import math
import settle
import scipy.special as sp

# Size distribution data source for speaking and coughing: https://www.sciencedirect.com/science/article/pii/S0021850208002036?via%3Dihub
# Size distribution data source for breathing was visually recovered from Fig 4&5: https://doi.org/10.1016/j.jaerosci.2008.11.002

def speaking(T,RH):
    NaCl_con = 80.0/1000; # 80.0 mmol/L converted to mol/L for saliva, from Kallapur et al.
    sizeclass = [3,6,12,20,28,36,45,62.5,87.5,112.5,137.5,175,225,375,750] # in um
    numcon = [4.59,66.21,22.23,11.33,7.87,4.32,3.37,4.57,3.44,4.52,4.31,4.52,3.85,3.45,1.11] # in cm^-3
    #sizeclass = [12,20,28,36,45,62.5,87.5,112.5,137.5,175,225,375,750,1500] # in um
    #numcon = [22.23,11.33,7.87,4.32,3.37,4.57,3.44,4.52,4.31,4.52,3.85,3.45,1.11,0.00] # in cm^-3
    t_settle = []
    sizepeak = 6 
    for binnum in range(15):
        size = sizeclass[binnum]
        #eqsize = 2*10**6 * settle.kohler(T, RH, size, NaCl_con)
        count = numcon[binnum]
        settime = settle.settling_time(T,RH,size,NaCl_con,1.5,model='sc')
        #if eqsize > 10:
        #    settime = settle.settling_time(T,RH,size,NaCl_con,1.5,model='empirical_big')
        #else:
        #    settime = settle.settling_time(T,RH,size,NaCl_con,1.5,model='empirical_small') 
        #print(eqsize,settime)
        t_settle.append(settime)
    t_peak = settle.settling_time(T,RH,sizepeak,NaCl_con,1.5,model='sc')
    #eqsizepeak = 2*10**6 * settle.kohler(T, RH, sizepeak, NaCl_con)
    #if eqsizepeak > 10:
        #t_peak = settle.settling_time(T,RH,sizepeak,NaCl_con,1.5,model='empirical_big')
    #else:
        #t_peak = settle.settling_time(T,RH,sizepeak,NaCl_con,1.5,model='empirical_small')    
    return(sizeclass,numcon,t_settle,sizepeak,t_peak)

def coughing(T,RH):
    NaCl_con = 91.0/1000; # Didn't find any data on dry cough droplet sodium level, here I assume it's close to mouth breathing?
    sizeclass = [3,6,12,20,28,36,45,62.5,87.5,112.5,137.5,175,225,375,750,1500] # in um
    numcon = [86,1187,444,144,54,50,41,43,30,36,34,93,53,44,30,0] # in cm^-3
    t_settle = []
    sizepeak = 6
    for binnum in range(16):
        size = sizeclass[binnum]
        count = numcon[binnum]
        if size > 10:
            settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5,model='empirical_big')
        else:
            settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5,model='empirical_small')
        t_settle.append(settling_time)
        t_peak = settle.settling_time(T,RH,sizepeak,NaCl_con,1.5,model='empirical_big')
    return(sizeclass,numcon,t_settle,sizepeak,t_peak)

# Breathing not ready yet. Need to verify the numbers are comparible to the other two modes, i.e. per 
# def breathing(T,RH):
#     NaCl_con = 91.0/1000; # 91 mmol/L converted to mol/L for exhaled condensate, from Effros et al. The paper didn't explicitly state, but it looks like mouth breathing to me.
#     logD = np.arange(-0.3,1.1,0.1)
#     sizeclass = 10**(logD) # in um
#     numcon = [86,1187,444,144,54,50,41,43,30,36,34,93,53,44,30,0] # in cm^-3
#     t_settle = []
#     for binnum in range(14):
#         size = sizeclass[binnum]
#         count = numcon[binnum]
#         settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5)
#         t_settle.append(settling_time)
#     return(sizeclass,numcon,t_settle)

def sknorm(x,A,mu,sig):
    yfit = A*np.exp(-(x - mu)**2 / (2 * sig**2))
    #normpdf = (1/(sig*np.sqrt(2*math.pi)))*np.exp(-(np.power((x-mu),2)/(2*np.power(sig,2))))
    #normcdf = (0.5*(1+sp.erf((alpha*((x-mu)/sig))/(np.sqrt(2)))))
    #return 2*A*normpdf*normcdf + c
    return yfit

    
def gfit(x,y,parameters):
    A = parameters[0]
    mu = parameters[1]
    sig = parameters[2]
    yfit = A*np.exp(-(x - mu)**2 / (2 * sig**2))
    residuals = y - yfit
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y-np.mean(y))**2)
    rsq = 1 - (ss_res / ss_tot)
    return rsq




