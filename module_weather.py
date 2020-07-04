#!/usr/bin/env python
# coding: utf-8

# In[116]:


import csv
import numpy as np
import matplotlib.pyplot as plt
# Weather data source:
# https://www.ncdc.noaa.gov/cdo-web/datatools/lcd

from datetime import date
from datetime import timedelta 


# The weather data file contains data from 2/1/2020 to 4/30/2020

def weatherdataprocess(filename,input_date0,input_date1):
    weatherdata = []
    with open(filename) as weather_data_file:
        metadata = csv.reader(weather_data_file, delimiter=',')
        for item in metadata:
            weatherdata.append(item)
    num_records = len(weatherdata)   
    columnhead = weatherdata[0]
    recorddata = weatherdata[1:num_records]

    date0 = np.fromstring(input_date0, dtype=int, sep="/")
    date1 = np.fromstring(input_date1, dtype=int, sep="/")
    d0 = date(2000+date0[2],date0[0],date0[1])+timedelta(days=14)
    d1 = date(2000+date1[2],date1[0],date1[1])+timedelta(days=14)
    tempdata = []
    RHdata = []
    
    for num in range(2737): # modified here to use only febuary part of the data
        pull_a_record = recorddata[num]
        d_rec = np.fromstring(pull_a_record[1], dtype=int, sep="-")
        drec = date(d_rec[0],d_rec[1],d_rec[2])
        if drec >= d0:
            if drec <= d1:
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




