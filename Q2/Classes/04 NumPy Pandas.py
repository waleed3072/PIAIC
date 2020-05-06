#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
arr = np.arange(16).reshape((2,2,4))
arr.transpose((1,0,2))


# In[2]:


arr


# In[3]:


arr.transpose((1,2,0))


# In[4]:


arr = np.arange(32).reshape((4,4,2))
arr


# In[5]:


arr.transpose((1,2,0))


# In[6]:


arr.swapaxes(1,2)


# In[11]:


get_ipython().system('type examples/ex1.csv')


# In[12]:


pd.read_csv('examples/ex1.csv')


# In[13]:


pd.read_table('examples/ex1.csv', sep=',')


# In[14]:


pd.read_csv('examples/ex2.csv', header=None)


# In[15]:


pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])


# In[16]:


pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'], index_col='message')


# In[18]:


pd.read_csv('examples/ex1.csv',index_col='b')


# In[19]:


pd.read_csv('examples/csv_mindex.csv',index_col=['key1', 'key2'])


# In[20]:


pd.read_csv('examples/csv_mindex.csv')


# In[21]:


pd.read_csv('examples/csv_mindex.csv',index_col=['key1'])


# In[22]:


pd.read_table('examples/ex3.txt', sep='\s+')


# In[23]:


pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3])


# In[24]:


pd.read_csv('examples/ex5.csv')


# In[25]:


pd.isnull(pd.read_csv('examples/ex5.csv'))


# In[26]:


pd.read_csv('examples/ex5.csv', na_values=['NULL'])


# In[27]:


pd.read_csv('examples/ex5.csv', na_values={'message': ['foo', 'NA'], 'something': ['two']})


# In[ ]:




