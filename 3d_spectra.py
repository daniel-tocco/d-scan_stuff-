#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os 
from mpl_toolkits import mplot3d

def plot_data_dBs_3d(file_):
    df = pd.read_csv(file_, skiprows=39, header=None)
    x = np.array(df[0][:]) 
    y = np.array(df[1][:])
    y_sum = sum(y)
    if 'W0000' in file_:
        df['disp_val'] = -1.0
        
    elif 'W0001' in file_:
        df['disp_val'] = -0.95
    
    elif 'W0002' in file_:
        df['disp_val'] = -0.9
    
    elif 'W0003' in file_:
        df['disp_val'] = -0.85
        
    elif 'W0004' in file_:
        df['disp_val'] = -0.8
        
    elif 'W0005' in file_:
        df['disp_val'] = -0.75
    
    elif 'W0006' in file_:
        df['disp_val'] = -0.7
    
    elif 'W0007' in file_:
        df['disp_val']= -0.65
    
    elif 'W0008' in file_:
        df['disp_val'] = -0.6
        
    elif 'W0009' in file_:
        df['disp_val'] = -0.55
        
    elif 'W0010' in file_:
        df['disp_val'] = -0.5
        
    elif 'W0011' in file_:
        df['disp_val'] = -0.45
    
    elif 'W0012' in file_:
        df['disp_val'] = -0.4
    
    elif 'W0013' in file_:
        df['disp_val'] = -0.35
        
    elif 'W0014' in file_:
        df['disp_val']= -0.3
        
    elif 'W0015' in file_:
        df['disp_val'] = -0.25
        
    elif 'W0016' in file_:
        df['disp_val'] = -0.2
    
    elif 'W0017' in file_:
        df['disp_val'] = -0.15
    
    elif 'W0018' in file_:
        df['disp_val'] = -0.1
        
    elif 'W0019' in file_:
        df['disp_val'] = -0.05
        
    elif 'W0020' in file_:
        df['disp_val'] = 0
        
    elif 'W0021' in file_:
        df['disp_val'] = 0.05
    
    elif 'W0022' in file_:
        df['disp_val'] = 0.1
    
    elif 'W0023' in file_:
        df['disp_val'] = 0.15
        
    elif 'W0024' in file_:
        df['disp_val'] = 0.2
        
    elif 'W0025' in file_:
        df['disp_val'] = 0.25
        
    elif 'W0026' in file_:
        df['disp_val'] = 0.3
        
    elif 'W0027' in file_:
        df['disp_val'] = 0.35
    
    elif 'W0028' in file_:
        df['disp_val'] = 0.4
    
    elif 'W0029' in file_:
        df['disp_val'] = 0.45
        
    elif 'W0030' in file_:
        df['disp_val'] = 0.5
        
    elif 'W0031' in file_:
        df['disp_val'] = 0.55
        
    elif 'W0032' in file_:
        df['disp_val'] = 0.6
    
    elif 'W0033' in file_:
        df['disp_val'] = 0.65
    
    elif 'W0034' in file_:
        df['disp_val'] = 0.7
        
    elif 'W0035' in file_:
        df['disp_val'] = 0.75
        
    elif 'W0036' in file_:
        df['disp_val'] = 0.8
        
    elif 'W0037' in file_:
        df['disp_val'] = 0.85
    
    elif 'W0038' in file_:
        df['disp_val'] = 0.9
    
    elif 'W0039' in file_:
        df['disp_val'] = 0.95
        
    elif 'W0040' in file_:
        df['disp_val'] = 1
    
    plt.plot(x, df['disp_val'], y)
    

    
    
    


# In[6]:


get_ipython().run_line_magic('matplotlib', 'qt')

for articles in os.listdir("C:/Users/Dan/Downloads/article_measurements/article_measurements"):
    for powers in os.listdir("C:/Users/Dan/Downloads/article_measurements/article_measurements/" + articles):
        
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_zlim(-100, 25)
        for disp_vals in os.listdir("C:/Users/Dan/Downloads/article_measurements/article_measurements/" + articles + '/' + powers):
            plot_data_dBs_3d("C:/Users/Dan/Downloads/article_measurements/article_measurements/" + articles + '/' + powers + '/' + disp_vals)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




