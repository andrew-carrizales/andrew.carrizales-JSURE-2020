# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:08:28 2020

@author: carra
"""
#my data

import numpy as np
from math import log
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(ym,t):
#    a = 0.9
    b = 100000
   
    if t <=3: 
       a = 0.85
    else:
       a =0.5
       
    dydt = log(2)/a *ym*(1-ym/b)
    return dydt

# initial condition
y0 = 3250


# time points
t = np.linspace(0,6)

# solve ODE
ym = odeint(model,y0,t)

# plot data
td = [1,2,3,4,5,6]
yd = [20000,8750,36250,70000,111250,252500]
plt.plot(td,yd,'*')

# plot results
plt.plot(t,ym)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()