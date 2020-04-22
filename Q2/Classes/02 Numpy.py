#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
matrix = np.random.randn(3,2)
matrix


# In[3]:


np.transpose(matrix)


# In[14]:


get_ipython().run_line_magic('time', 'np.arange(1,7).reshape((3,2))')


# In[12]:


np.transpose(matrix)


# In[15]:


np.arange(1,7).reshape((3,2))


# In[46]:


matrix = np.arange(1,37).reshape((3,4,3))
matrix.transpose((0,1,2))
matrix


# In[48]:


np.arange(1,13,dtype='float').reshape((3,4))


# In[ ]:




