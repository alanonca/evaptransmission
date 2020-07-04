#!/usr/bin/env python
# coding: utf-8

import csv
import numpy as np
import matplotlib.pyplot as plt

# COVID cases data source:
# https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/

from datetime import date
from datetime import timedelta 


def confirmedcases(countyname,input_date0,input_date1): # Extract confirmed cases in a county from date0 to date1 
    
    with open('covid_confirmed_usafacts.csv') as covid_data_file:
        metadata = csv.reader(covid_data_file, delimiter=',')
        extractdata = []
        for item in metadata:
            extractdata.append(item)
    num_records = len(extractdata) 
    columnhead = extractdata[0]
    recorddata = extractdata[1:num_records]
    dateseries = []

    for num in range(num_records-1):
        record = recorddata[num]
        if record[1] == countyname:
            for datenum in range(len(columnhead)):
                datadate = columnhead[datenum]
                if input_date0 == datadate:    
                    date0 = np.fromstring(input_date0, dtype=int, sep="/")
                    date1 = np.fromstring(input_date1, dtype=int, sep="/")
                    d_data0 = date(2020,1,22)
                    d0 = date(2000+date0[2],date0[0],date0[1])+timedelta(days=14)
                    d1 = date(2000+date1[2],date1[0],date1[1])+timedelta(days=14)
                    date0_numindata = d0 - d_data0
                    delta = d1 - d0
                    cases_sub = record[3 + date0_numindata.days : 4 + date0_numindata.days + delta.days]
                    cases = record[4 + date0_numindata.days : 5 + date0_numindata.days + delta.days]
                                            
    cases = np.array(cases).astype(np.float)
    cases_sub = np.array(cases_sub).astype(np.float)
    newcases = cases - cases_sub
    nc_perc = newcases/cases_sub #Percent of newcases to yesterday's total
    return [dateseries,cases,newcases,nc_perc]

