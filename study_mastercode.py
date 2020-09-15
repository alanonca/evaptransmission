#!/usr/bin/env python
# coding: utf-8

# In[11]:


import settle
import viability
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import savetxt
import math

import module_weather
import module_initsize
import module_covidstats
import module_riskfactor
import viability

import timeseries #AG



# Input section: county to be studied, weather date range, transmission mode
countyname = 'Los Angeles County' # Input 'King County' , 'Los Angeles County' , 'Miami-Dade County', 'Maricopa County', 'Harris County', 'San Diego County', 'Clark County', or 'Santa Clara County'.
offset = 0
input_date0 = '4/1/20' # for weather data range. Avoid 3/8 for LA in the time range, no RH data for that day.
input_date1 = '4/29/20'
mode_to_test = 'speaking' # Input'speaking','coughing', or 'breathing'



# Load weather data

if countyname == 'Los Angeles County':
    filename = 'LAweather.csv'
elif countyname == 'King County':
    filename = 'KCweather.csv'
elif countyname == 'Miami-Dade County':
    filename = 'MIAweather.csv'
elif countyname  == 'Maricopa County':
    filename = 'MARIweather.csv'
elif countyname  == 'Harris County':
    filename = 'HARweather.csv'
elif countyname  == 'San Diego County':
    filename = 'SDweather.csv'
elif countyname  == 'Clark County':
    filename = 'CLARKweather.csv'
elif countyname  == 'Santa Clara County':
    filename = 'SCweather.csv' 
    
[tempC,RH] = module_weather.weatherdataprocess(filename,input_date0,input_date1) 

module_weather.weatherdatapplot(tempC,RH)



# Calculate daily settling time for the transmission mode of study

tset = []
viab_hl = []
risk_fac = []

for day in range(len(tempC)):
    daily_T = tempC[day]
    daily_RH = RH[day]
    if mode_to_test == 'speaking':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.speaking(daily_T,daily_RH)
    elif mode_to_test == 'coughing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.coughing(daily_T,daily_RH)
    elif mode_to_test == 'breathing':
        [sizeclass,numcon,t_settle,sizepeak,t_peak] = module_initsize.breathing(daily_T,daily_RH)
    #popt, pcov = curve_fit(module_initsize.gaussian, t_settle, numcon)
    #daily_tset = popt[1]
    #tset.append(daily_tset)
    tset.append(t_peak)
    
    #Calculate virus half life everyday 
    decay_rate = viability.kdecay(daily_T,daily_RH,0)
    halflife = math.log(2)/decay_rate
    viab_hl.append(halflife)
    
    #Calculate risk factor everyday
    risk = module_riskfactor.riskfactor2(daily_T,daily_RH,mode_to_test)
    risk_fac.append(risk)
    
    

plt.plot(tset)
plt.ylabel('Daily droplet settling time in hr')
plt.show()

plt.plot(viab_hl)
plt.ylabel('Daily virus half-life in min')
plt.show()

plt.plot(risk_fac)
plt.ylabel('Daily risk factor')
plt.show()

# Load corresponding COVID-19 data
[dateseries,cases,activecases,dailynew,nc_perc] = module_covidstats.confirmedcases(countyname,input_date0,input_date1)
plt.plot(dailynew)
plt.ylabel('Daily new confirmed cases')
plt.show()

plt.plot(nc_perc)
plt.ylabel('Daily percent new cases')
plt.show()

plt.scatter(tset,dailynew)
plt.ylabel('Daily new confirmed cases v.s. settling time')
plt.show()

plt.scatter(tset,nc_perc)
plt.ylabel('Daily percent new cases v.s. settling time')
plt.show()

plt.scatter(viab_hl,dailynew)
plt.ylabel('Daily new confirmed cases v.s. virus half-life')
plt.show()

plt.scatter(viab_hl,nc_perc)
plt.ylabel('Daily percent new cases v.s. virus half-life')
plt.show()

plt.scatter(risk_fac,dailynew)
plt.ylabel('Daily new confirmed cases v.s. risk factor')
plt.show()

plt.scatter(risk_fac,nc_perc)
plt.ylabel('Daily percent new cases v.s. risk factor')
plt.show()


# Compile and output into a CSV file
# outputdata = [tset,viab_hl,risk_fac,nc_perc]
outputdata = [tset,viab_hl,nc_perc]
#print(outputdata)


# In[12]:


savetxt('output.csv', outputdata, delimiter=',')

# In[ ]:




#AG
print('offset by %.2i days' % offset)
# def comparison(data1[array], data2[array], offset[days]):
[corr_pearson, pval_pearson, corr_spearman, pval_spearman] = timeseries.comparison(tset,nc_perc,offset)
print('Pearsons correlation: %.3f' % corr_pearson)
print('Pearsons p value: %.3f' % pval_pearson)
print('Spearmans correlation: %.3f' % corr_spearman)
print('Spearmans p value: %.3f' % pval_spearman)
print('')