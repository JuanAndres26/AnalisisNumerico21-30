# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 13:56:33 2021

@author: casta
"""

from scipy.stats import binom
import seaborn as sb

binom.rvs(size=10,n=1000,p=0.5)

data_binom = binom.rvs(n=1000,p=0.5,loc=0,size=1000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='blue',
                  hist_kws={"linewidth": 16,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')