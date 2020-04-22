#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


np.sum([1,3])


# In[1]:


sum([1,3])


# In[2]:


def abc():
    print("hello")
    
def abc():
    print("Pakistan")
    
abc()    


# In[5]:


np.__version__


# In[6]:


get_ipython().system('pip install --upgrade numpy')


# In[7]:


get_ipython().run_line_magic('history', '')

%run abc.py
%load abc.py
# In[9]:


get_ipython().run_line_magic('time', 'list(range(2000000))[:20]')


# In[10]:


get_ipython().run_line_magic('time', 'np.arange(2000000)')


# In[12]:


get_ipython().run_line_magic('time', '[x+5 for x in range(1,1000000)][:20]')


# In[26]:


l = list(range(1,1000000))
l2 = list(enumerate(l))
for i, v in l2:
    l[i] = l[i]+5
l[:20] 
get_ipython().run_line_magic('time', '')


# In[47]:


# Two Dimension list adding value 5 

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print("Before Adding 5")
print(a)
print()
for r, rd in list(enumerate(a)):
    for c, cd in list(enumerate(rd)):
        a[r][c] = a[r][c] + 5
        
print("After Adding 5")        
print(a) 


# In[48]:


a = np.arange(1,10).reshape((3,3))
a = a+5
a


# In[52]:


a = np.arange(1,28).reshape((3,3,3))
a = a+5
a


# In[61]:


a = np.arange(1,28).reshape((3,3,3))
a = a%2
a


# In[70]:


a = np.random.randn(2,3,3,4,5,5)
print(a.ndim)
print(a.shape)
a = a * 10
a


# In[75]:


a = np.arange(1,13).reshape((6,2))
print(a)

print(a * a)


# # a[i,j,k]

# In[55]:


#a[2]
#a[2,0]
a[2,0,1]

<img src="https://www.pythoninformer.com/img/numpy/3d-array.png">
# <img src="https://www.pythoninformer.com/img/numpy/3d-array.png">

# In[ ]:





# In[27]:


l = np.arange(1,1000000)
l = l + 5
l


# In[28]:


type(l)


# In[29]:


l.shape


# In[31]:


l.ndim


# # Dimensions

# In[33]:


a = np.array([1])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)


# In[34]:


a = np.array([1,2,4,5])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)


# In[36]:


a = np.array([[1,2,4],
              [3,5,6],
              [2,1,5]])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)


# # Creating ndarrays

# In[78]:


a = [1,2,3]
print(type(a))

a = np.array(a)
type(a)


# In[79]:


a = (1,2,3)

print(type(a))

a = np.array(a)
type(a)


# In[80]:


a = {1,2,3}
print(type(a))

a = np.array(a)
type(a)


# # np.array

# In[83]:


l = [1,2,3]
a = np.array(l)
b = np.array(a)
a is b


# ### np.asarray

# In[84]:


l = [1,2,3]
a = np.asarray(l)
b = np.asarray(a)
a is b


# In[ ]:




