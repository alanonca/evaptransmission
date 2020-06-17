#!/usr/bin/env python
# coding: utf-8

# In[116]:


import csv
import numpy as np
import matplotlib.pyplot as plt
# Weather data source:
# https://www.ncdc.noaa.gov/cdo-web/datatools/lcd


# In[119]:


# Here consider Feb 1 as Day 1, different for a new data file
def weatherdataprocess(filename):
    weatherdata = []
    with open(filename) as weather_data_file:
        metadata = csv.reader(weather_data_file, delimiter=',')
        for item in metadata:
            weatherdata.append(item)
    num_records = len(weatherdata)   
    columnhead = weatherdata[0]
    recorddata = weatherdata[1:num_records]
    
    tempdata = []
    RHdata = []
    for num in range(850): # modified here to use only febuary part of the data
        pull_a_record = recorddata[num]
        if pull_a_record[2] == 'SOD  ':#to read 'summary of the day' data only for daily average temp and RH
            tempdata.append(pull_a_record[19])
            RHdata.append(pull_a_record[20])
    temp = np.array(tempdata) 
    temp = temp.astype(np.float)
    tempC = (temp-32)*5/9
    RH = np.array(RHdata)
    RH = RH.astype(np.float)
    
    return [tempC,RH]


# In[113]:


def weatherdatapplot(tempC,RH):
    plt.plot(tempC)
    plt.ylabel('Daily Temperature in C')
    plt.show()

    plt.plot(RH)
    plt.ylabel('Daily Relative Humidity in %')
    plt.show()


# In[ ]:




