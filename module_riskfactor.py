#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Here are function for a few risk factor definitions:
# riskfactor: at 10 min, summing up for all droplet sizes,  the viable particle counts per cm3 air, times 1 minus the ratio of 10min to settling time
# riskfactor2: at 10 min, summing up for all droplet sizes,  the viable particle counts per cm3 air, times the square of 1 minus the ratio of 10min to settling time


import module_initsize
import numpy as np
import settle
import viability

def riskfactor(T,RH,mode):
    
    mode_to_test = mode
    risk_fac = 0
    
    if mode_to_test == 'speaking':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.speaking(T,RH)
        NaCl_con = 80.0/1000; # 80.0 mmol/L converted to mol/L for saliva, from Kallapur et al.
    elif mode_to_test == 'coughing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.coughing(T,RH)
        NaCl_con = 91.0/1000; # Didn't find any data on dry cough droplet sodium level, here I assume it's close to mouth breathing?
    elif mode_to_test == 'breathing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.breathing(T,RH)
    viralload = 10**8 # viral particles per mL saliva
    
    for binnum in range(len(sizeclass)):
        size = sizeclass[binnum]
        count = numcon[binnum]
        dropvol = 4/3 * np.pi*((size/2)**3) * (10**(-12)) # droplet volume converted to mL
        poi_lambda = viralload * dropvol # in viral particles per droplet
        decay_rate = viability.kdecay(T,RH,1.9)
        if size > 10:
            settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5,model='empirical_big')
        else:
            settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5,model='empirical_small')
        viable_numcon_10min = count*poi_lambda* np.exp(- decay_rate * (1/6) * 60) 
        risk_10min = viable_numcon_10min * np.maximum(1-((1/6)/settling_time),0)
        risk_fac = risk_fac + risk_10min # sum up the risk factors for a total risk at this T and RH condition
    
    return risk_fac

def riskfactor2(T,RH,mode):
    
    mode_to_test = mode
    risk_fac = 0
    
    if mode_to_test == 'speaking':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.speaking(T,RH)
        NaCl_con = 80.0/1000; # 80.0 mmol/L converted to mol/L for saliva, from Kallapur et al.
    elif mode_to_test == 'coughing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.coughing(T,RH)
        NaCl_con = 91.0/1000; # Didn't find any data on dry cough droplet sodium level, here I assume it's close to mouth breathing?
    elif mode_to_test == 'breathing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.breathing(T,RH)
    viralload = 10**8 # viral particles per mL saliva
    
    for binnum in range(len(sizeclass)):
        size = sizeclass[binnum]
        count = numcon[binnum]
        dropvol = 4/3 * np.pi*((size/2)**3) * (10**(-12)) # droplet volume converted to mL
        poi_lambda = viralload * dropvol # in viral particles per droplet
        decay_rate = viability.kdecay(T,RH,1.9)
        if size > 10:
            settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5,model='empirical_big')
        else:
            settling_time = settle.settling_time(T,RH,size,NaCl_con,1.5,model='empirical_small')
        viable_numcon_10min = count*poi_lambda* np.exp(- decay_rate * (1/6) * 60) 
        risk_10min = viable_numcon_10min * (np.maximum(1-((1/6)/settling_time),0)**2)
        risk_fac = risk_fac + risk_10min # sum up the risk factors for a total risk at this T and RH condition
    
    return risk_fac

