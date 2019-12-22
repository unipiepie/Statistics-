#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats


# In[ ]:


#一般正态分布
plt.figure()
std = 1
mean = 2
normalDistribution = stats.norm(mean, std)                # 构建统计分布
x = np.linspace(normalDistribution.ppf(0.01), normalDistribution.ppf(0.99), 100)
plt.plot(x, stats.normalDistribution.pdf(x))


# In[3]:


#标准正态分布
plt.subplot2grid((2, 2), (0, 1))
# print(norm.ppf(0.6179))                        # 知道q时求x, q=a
# print(norm.cdf(0.3))                           # 知道x时求q
x = np.linspace(stats.norm.ppf(0.01), stats.norm.ppf(0.99), 100)
plt.plot(x, stats.norm.pdf(x), alpha=0.6, label='norm pdf')


# In[5]:


#T分布
plt.subplot2grid((2, 2), (1, 0))
df = 15
x = np.linspace(stats.t.ppf(0.01, df), stats.t.ppf(0.99, df), 100)
# print(t.ppf(0.95, df))        # q=0.95,a=(1-q)*2
# print(t.cdf(1.753, df))
plt.plot(x, stats.t.pdf(x, df), alpha=0.6, label='t pdf')


# In[6]:


#F分布
plt.subplot2grid((2, 2), (1, 1))
df = 5
dn = 8
x = np.linspace(stats.f.ppf(0.01, df, dn), stats.f.ppf(0.99, df, dn), 100)
# print(f.ppf(0.95, df, dn))
plt.plot(x, stats.f.pdf(x, df, dn), alpha=0.6, label='f pdf')


# In[ ]:


#卡方分布
df = pd.read_excel('/Users/Downloads/data.xlsx',usecols = [1,2,3] )

plt.figure()
plt.subplot2grid((2, 2), (0, 0))
df = 20               # 自由度
# print(chi2.ppf(0.01, df))        # 计算函q=0.01概率时数值。其中 q = 1-a
# print(chi2.cdf(8.260, df))       # 知道x值求a
x = np.linspace(stats.chi2.ppf(0.01, df),                       # 绘制概率密度图
                 stats.chi2.ppf(0.99, df), 100)
plt.plot(x, stats.chi2.pdf(x, df), alpha=0.6, label='chi2 pdf')

