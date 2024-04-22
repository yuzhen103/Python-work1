#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('C:/Users/UESR/Desktop/FL_insurance_sample.csv', sep=',', nrows=10)


# In[3]:


df.head(10)


# In[9]:


import pandas as pd
import numpy as np


# In[10]:


data=np.random.randint(1,10,(5,3))
df=pd.DataFrame(data, columns=list('ABC'))
df


# In[11]:


df.to_csv("spam.csv")


# In[12]:


df_load=pd.read_csv("spam.csv")


# In[13]:


df_load


# In[14]:


get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# In[15]:


df_load=pd.read_csv("spam.csv", index_col=0)


# In[16]:


df_load


# In[ ]:




