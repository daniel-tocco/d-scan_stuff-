#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os

def calc_Pout(file_):
        df = pd.read_csv(file_, skiprows=39, header=None)
        x = np.array(df[0][:]) 
        y = np.array(10**(df[1][:]/10.0))
        Pout = 60/(0.1 * 6001)*sum(y)
        output_powers.append(Pout)
    
    


input_powers = [70, 130, 180, 280, 350, 550]
for articles in os.listdir("C:/Users/Dan/Downloads/article_measurements/article_measurements"):
    output_powers = []
    for powers in os.listdir('C:/Users/Dan/Downloads/article_measurements/article_measurements/' + articles):
        for dispersions in os.listdir('C:/Users/Dan/Downloads/article_measurements/article_measurements/' + articles + '/' + powers): 
            if 'W0000' in dispersions:
                calc_Pout("C:/Users/Dan/Downloads/article_measurements/article_measurements/" + articles + '/' + powers + '/' + dispersions)
            else: 
                pass
            
    plt.figure()
    plt.grid()
    plt.title(powers)
    plt.xlabel('Pin (mW)')
    plt.ylabel('Pout (mW)')
    plt.plot(input_powers, output_powers, linestyle='-', marker='s')

