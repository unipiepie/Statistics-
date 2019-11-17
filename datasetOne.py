#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Achieve Descriptive statistics
#Reference: https://blog.csdn.net/qq_43315928/article/details/102151709


# In[30]:


import pandas as pd
import numpy as np


# In[31]:


path = "C:\\Users\\tatapie\\Desktop\\Statistics\\datasetOne.xlsx"
#.iloc Select the whole column
data = pd.read_excel(path)
data


# In[63]:


#Arithmetic Average
#Method one
print("Arithmetic Average: %.2f"%data.mean())
#Geometric Mean
# 几何平均数
"""
import math
s = 1
for i in data:
    s *= i
print('几何平均数为：', math.pow(s, 1/len(data)))
"""


# In[38]:


# 众数
# 法一：
print("众数为：%d," %data.mode().iloc[0])
# 法二
from scipy.stats import mode
mode_num = mode(data)
print("众数为：%d, 众数的个数为：%d,"%(mode_num[0][0], mode_num[1][0]))

print(mode_num)
print(data.mode())


# In[39]:


# 中位数
# 法一：
print("中位数1:%d" %data.median())
# 法二
print("中位数2:%d" %np.percentile(data,50))
# 法三
print("中位数3:%d" %data.quantile(.50))


# In[42]:


# 分位数
# 法一
print('下四分位数为：', np.percentile(data, 25))
print('上四分位数为：', np.percentile(data, 75))
# 法二
print('下四分位数为：', data.quantile(.25))
print('上四分位数为：', data.quantile(.75))


# In[48]:


# 方差
print("方差：%d" %data.var())


# In[46]:


# 标准差
# 法一
print("标准差:%d" %data.std())


# In[49]:


# 分位数
# 法一
print('下四分位数为：', np.percentile(data, 25))
print('上四分位数为：', np.percentile(data, 75))
# 法二
print('下四分位数为：', data.quantile(.25))
print('上四分位数为：', data.quantile(.75))


# In[51]:


# 众数
from collections import Counter
count = Counter(data)
modeCount = count.most_common(1)[0][1]
totalCount = len(data)
# 异众比率
ratio = (totalCount - modeCount) / totalCount
print(ratio)


# In[52]:


# 四分位差
# 法一
print('四分位差为：', np.percentile(data, 75) - np.percentile(data, 25))
# 法二
print('四分位差为：', data.quantile(.75) - data.quantile(.25))


# In[53]:


# 极差
print('极差为：', data.max() - data.min())


# In[56]:


#偏度
from scipy import stats
print('偏度为：', stats.skew(data))


# In[57]:


# 峰度
print('峰度为：', stats.kurtosis(data))


# In[ ]:




