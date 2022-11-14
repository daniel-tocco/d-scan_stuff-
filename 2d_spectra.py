#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os 

x_array = []
y_array = []
disp_array = []

    
def plot_data_dBs(file_):
    df = pd.read_csv(file_, skiprows=39, header=None)
    x = np.array(df[0][:]) 
    y = np.array(df[1][:])
    y_sum = sum(y)
    plt.figure(1)
    plt.plot(x, y)
    plt.show()
    
def plot_data_Watts(file_):
    df = pd.read_csv(file_, skiprows=39, header=None)
    x = np.array(df[0][:]) 
    y = np.array(10**(df[1][:]/10.0))
    y_sum = sum(y)
    disp_val = np.array(df[2][0])
    plt.plot(x, y, disp_val)
    plt.show()


# In[25]:


for articles in os.listdir("C:/Users/Dan/Downloads/article_measurements/article_measurements"):
    for powers in os.listdir("C:/Users/Dan/Downloads/article_measurements/article_measurements/" + articles):
        for disp_vals in os.listdir("C:/Users/Dan/Downloads/article_measurements/article_measurements/" + articles + '/' + powers):
            plot_data_dBs("C:/Users/Dan/Downloads/article_measurements/article_measurements/" + articles + '/' + powers + '/' + disp_vals)

