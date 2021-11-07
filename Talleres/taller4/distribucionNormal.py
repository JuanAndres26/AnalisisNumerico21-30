# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 11:54:24 2021

@author: casta
"""

import numpy as np
import matplotlib.pyplot as plt

class norm1:
    def __init__(a1, b1, c1):
        a1 = a1
        b1 = b1
        c1 = c1
        
    def dist_curve(self):
        plt.plot(self.c1, 1/(self.b1 * np.sqrt(2 * np.pi)) *
            np.exp( - (self.c1 - self.a1)**2 / (2 * self.b1**2) ), linewidth=3, color='y')
        plt.show()

#Vary the mean and SD to generate different plots
mean1 = 0.5
sd1 = 0.05

c = np.random.normal(mean1, sd1, 1000)
        
w1, x1, z1 = plt.hist(c, 100, normed=True) #hist

hist1 = norm1(mean1, sd1, x1)
plot1 = hist1.dist_curve()