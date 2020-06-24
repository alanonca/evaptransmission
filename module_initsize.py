#!/usr/bin/env python
# coding: utf-8

# In[74]:


import csv
import numpy as np
import settle

# Size distribution data source for speaking and coughing: https://www.sciencedirect.com/science/article/pii/S0021850208002036?via%3Dihub
# Size distribution data source for breathing was visually recovered from Fig 4&5: https://doi.org/10.1016/j.jaerosci.2008.11.002

def speaking(T,RH):
    NaCl_con = 80.0/1000; # 80.0 mmol/L converted to mol/L for saliva, from Kallapur et al.
    sizeclass = [3,6,12,20,28,36,45,62.5,87.5,112.5,137.5,175,225,375,750,1500] # in um
    numcon = [4.59,66.21,22.23,11.33,7.87,4.32,3.37,4.57,3.44,4.52,4.31,4.52,3.85,3.45,1.11,0.00] # in cm^-3
    t_settle = []
    for binnum in range(16):
        size = sizeclass[binnum]
        count = numcon[binnum]
        settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5)
        t_settle.append(settling_time)
    return(sizeclass,numcon,t_settle)

def coughing(T,RH):
    NaCl_con = 91.0/1000; # Didn't find any data on dry cough droplet sodium level, here I assume it's close to mouth breathing?
    sizeclass = [3,6,12,20,28,36,45,62.5,87.5,112.5,137.5,175,225,375,750,1500] # in um
    numcon = [86,1187,444,144,54,50,41,43,30,36,34,93,53,44,30,0] # in cm^-3
    t_settle = []
    for binnum in range(16):
        size = sizeclass[binnum]
        count = numcon[binnum]
        settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5)
        t_settle.append(settling_time)
    return(sizeclass,numcon,t_settle)

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

def gaussian(x,A,mu,sig):
    yfit = A*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    return yfit

def gfit(x,y,parameters):
    A = parameters[0]
    mu = parameters[1]
    sig = parameters[2]
    yfit = A*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    residuals = y - yfit
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y-np.mean(y))**2)
    rsq = 1 - (ss_res / ss_tot)
    return rsq


# In[73]:





# In[ ]:





# In[ ]:




