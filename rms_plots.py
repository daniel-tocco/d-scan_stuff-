#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os


def calc_rms(file_):
    df = pd.read_csv(file_, skiprows=39, header=None)
    x = np.array(df[0][:]) 
    y = np.array(10**(df[1][:]/10.0)) 
    first_term = []    #the first_term and second_term stuff refers to the first and second terms in the rms equation
    second_term = [] 
    power = []

    for i in range(len(x)):
        first_term.append(y[i] * x[i]**2)
        second_term.append(y[i] * x[i])
        power.append(y[i])

    sum_first_term = sum(first_term)
    sum_second_term = sum(second_term)
    sum_power = sum(power)

    rms = 2*np.sqrt((sum_first_term / sum_power) - ((sum_second_term / sum_power) ** 2))
    rms_values.append(rms)

        
    
    
    

disp_vals = np.arange(-1, 1.05, 0.05)
for articles in os.listdir("C:/Users/Dan/Downloads/article_measurements/article_measurements"):
    for powers in os.listdir('C:/Users/Dan/Downloads/article_measurements/article_measurements/' + articles):
        rms_values = []
        for dispersions in os.listdir('C:/Users/Dan/Downloads/article_measurements/article_measurements/' + articles + '/' + powers): 
            calc_rms("C:/Users/Dan/Downloads/article_measurements/article_measurements/" + articles + '/' + powers + '/' + dispersions)
        
        if len(rms_values) != 41:
            pass
        else:
            plt.figure()
            plt.grid()
            plt.title(powers)
            plt.xlabel('Dispersion (ps/nm)')
            plt.ylabel('2\u03C3\u03BB')
            plt.plot(disp_vals, rms_values, linestyle='-', marker='s')



# In[ ]:




