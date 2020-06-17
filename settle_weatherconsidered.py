#!/usr/bin/env python
# coding: utf-8

# In[14]:


import settle
import viability
import weather
import matplotlib.pyplot as plt


# In[15]:


# Weather data for LA downtown in Febuary
filename = 'LADTweather.csv'# Input the .csv data file here

[tempC,RH] = weather.weatherdataprocess(filename)
t_settle = []
for day in range(len(tempC)):
    daily_T = tempC[day]
    daily_RH = RH[day]
    t = settle.settling_time(daily_T,daily_RH,10,0.05,1.5)
    t_settle.append(t)


# In[16]:


plt.plot(t_settle)
plt.ylabel('Daily Droplet Settling Time in hr')
plt.show()

weather.weatherdatapplot(tempC,RH)


# In[ ]:





# In[ ]:





# In[ ]:




