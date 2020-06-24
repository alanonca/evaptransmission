#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
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
# Breathing to be completed. Need to verify the numbers are comparible to the other two modes, i.e. per 
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


# In[59]:


mode_to_test = 'speaking' # enter 'speaking','coughing', or 'breathing'

T_range = [0.0,5,10,15,20,25,30,35]
RH_range = [10,20,30,40,50,60,70,80,90,100]

colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(T_range)))

for cond in range(len(T_range)): # Study the effect of varying temperature with fixed RH at 50% 
    T = T_range[cond]
    RH = 50
    if mode_to_test == 'speaking':
        [sizeclass,numcon,t_settle] = speaking(T,RH)
    elif mode_to_test == 'coughing':
        [sizeclass,numcon,t_settle] = coughing(T,RH)
    elif mode_to_test == 'breathing':
        [sizeclass,numcon,t_settle] = coughing(T,RH)
    c = colors[cond]
    plt.scatter(t_settle,numcon,color=c,s=5,label=str(T))
#label_list = [str(x) for x in T_range]
plt.axis([0, 0.005, 0, 70])
plt.title("Settling time distribution under varying temperature (with 50% RH)")
plt.xlabel('Settling time in hr')
plt.ylabel('Number concentration in cm^-3')
#plt.legend(label_list)
plt.legend(loc="upper right")
plt.show()

colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(RH_range)))

for cond in range(len(RH_range)): # Study the effect of varying RH with fixed T at 25 C
    T = 25
    RH = RH_range[cond]
    if mode_to_test == 'speaking':
        [sizeclass,numcon,t_settle] = speaking(T,RH)
    elif mode_to_test == 'coughing':
        [sizeclass,numcon,t_settle] = coughing(T,RH)
    elif mode_to_test == 'breathing':
        [sizeclass,numcon,t_settle] = coughing(T,RH)
    c = colors[cond]
    plt.scatter(t_settle,numcon,color=c,s=5,label=str(RH))
    
plt.axis([0, 0.005, 0, 70])
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




