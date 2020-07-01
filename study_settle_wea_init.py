#!/usr/bin/env python
# coding: utf-8

# In[1]:


import settle
import viability
import weather
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import module_initsize
import module_covidstats


# In[3]:



filename = 'LADTweather.csv'# Input the .csv data file here

[tempC,RH] = weather.weatherdataprocess(filename)
tset = []

mode_to_test = 'speaking' # Input'speaking','coughing', or 'breathing'

for day in range(len(tempC)):
    daily_T = tempC[day]
    daily_RH = RH[day]
    if mode_to_test == 'speaking':
        [sizeclass,numcon,t_settle] = module_initsize.speaking(daily_T,daily_RH)
    elif mode_to_test == 'coughing':
        [sizeclass,numcon,t_settle] = module_initsize.coughing(daily_T,daily_RH)
    elif mode_to_test == 'breathing':
        [sizeclass,numcon,t_settle] = module_initsize.breathing(daily_T,daily_RH)
    popt, pcov = curve_fit(module_initsize.gaussian, t_settle, numcon)
    daily_tset = popt[1]
    tset.append(daily_tset)


# In[4]:


plt.plot(tset)
plt.ylabel('Daily mean droplet settling time in hr')
plt.show()

weather.weatherdatapplot(tempC,RH)

countyname = 'Los Angeles County'
input_date0 = '3/15/20'
input_date1 = '4/15/20'

[total,dailynew] = module_covidstats.confirmedcases(countyname,input_date0,input_date1)
plt.plot(dailynew)
plt.ylabel('Daily new confirmed cases')
plt.show()




