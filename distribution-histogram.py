# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:37:16 2021

@author: Yz Zh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv("C:\\Users\\Yz Zh\\Desktop\\Shanghai\\park\\shanghai_park_size.csv")
data=np.array(data)

supply=[]
for item in data:
    supply.append(float(item))
    
bins=range(0,580,50)

plt.hist(x=supply,bins=bins,color='g',alpha=0.6)

plt.title("The distrbution of the size of parks (Shanghai)")
plt.xlabel("The size of the parks")
plt.ylabel("Count")
plt.show()