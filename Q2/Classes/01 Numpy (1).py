#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
a = np.arange(1,28).reshape((3,3,3))
print(a)


# In[4]:


print(a.shape)


# In[5]:


print(a.ndim)


# In[6]:


a += a
print(a)


# In[19]:


a = np.random.rand(3,4,5)
print(a)


# In[20]:


arr = [1,2,3]
print(type(a))


# In[21]:


a = np.array(a)
type(a)


# # np.array

# In[22]:


List = [1,2,3]
a = np.array(List)
a is List


# In[23]:


a is not List


# In[24]:


b = np.array(a)
a is b


# In[27]:


a = np.asarray(List)
b = np.asarray(a)
a is b


# In[28]:


get_ipython().run_line_magic('history', '')


# In[30]:


get_ipython().run_line_magic('time', 'list(range(10000000))[:20]')


# In[31]:


get_ipython().run_line_magic('time', 'np.arange(10000000)[:20]')


# In[32]:


print("Waleed\nButt")


# In[34]:


print("Waleed\\nButt")


# In[ ]:




