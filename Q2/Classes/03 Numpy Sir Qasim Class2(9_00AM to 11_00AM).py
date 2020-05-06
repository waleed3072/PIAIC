#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.arange(1,28).reshape((3,3,3))
a


# In[6]:


a.shape = (3,9)


# In[7]:


a


# In[8]:


np.zeros((3,3,3))


# In[9]:


np.zeros_like(a)


# In[11]:


np.ones((3,3,3,3))


# In[12]:


np.ones_like(a)


# In[13]:


np.empty((2,2))


# In[14]:


np.empty_like(a)


# In[15]:


np.full((2,3,3), fill_value=5)


# In[16]:


np.full_like(a, 7)


# In[17]:


np.ones((2,3)) * 7


# In[21]:


np.ones_like(a, dtype=np.float64)


# In[23]:


get_ipython().run_line_magic('pinfo2', 'np.eye')


# In[22]:


np.eye(6)


# In[24]:


np.identity(6)


# In[25]:


get_ipython().run_line_magic('pinfo2', 'np.identity')


# In[ ]:


from numpy import random


# # Data Types for ndarrays

# In[35]:


#reshape(astype(range(1,12)))
a = np.arange(1,13).astype(np.float64).reshape((3,4))
a


# In[36]:


a = np.arange(1,13).reshape((3,4)).astype(np.float64)
a


# In[44]:


a = np.arange(1,13).astype(np.character).reshape((3,4))
a


# In[40]:


a = np.arange(1,13, dtype="character").reshape((3,4))
a


# In[45]:


a = np.array([1,2,4], dtype=np.float32)
a


# In[46]:


arr2 = np.array([1, 2, 3], dtype=np.int32)
arr2


# In[48]:


print(a.dtype)
print(arr2.dtype)


# In[49]:


print(type(a))
print(type(a))


# In[55]:


a = np.array([1,2,3], dtype='int')
print(a.dtype)

a = np.array([1,2,3], dtype=np.int64)
print(a.dtype)
a = np.array([1,2,3], dtype='i8')
print(a.dtype)


# In[56]:


def abc(x):
    try:
        x = str(x)
        return np.int64("".join([i for i in x if str.isnumeric(i)]))
    except:
        return 0
    
abc("kjadjslkljskldksljkl3askjd-asdfl;ak3")    


# In[57]:


a = np.arange(1,12, dtype=np.float64)
b = np.arange(1,4)
print(a.dtype)
print(b.dtype)


# In[58]:


b.astype(a.dtype)


# In[59]:


a = np.arange(1,28).reshape((3,3,3))
a


# In[60]:


a % 5 == 0


# In[61]:


a[a % 5 == 0]


# In[62]:


a[(a%5==0) & (a%3==0)]


# In[63]:


a


# In[71]:


a[1][1][1]


# In[69]:


a[1:,1:,:1]


# In[72]:


a[1:][1:][1:]


# In[76]:


a[1:][1:][1:]


# In[70]:


a[1,1,1]


# # Class3

# In[1]:


l = [1,3,4,8,9]
l[:2] = 5


# In[2]:


import numpy as np


# In[3]:


l = np.array([1,3,4,8,9])
l[:2] = 5
l


# In[4]:


a = np.arange(3*4).reshape((3,4))
a


# In[8]:


print(a[:2])
print(a[0:2])
print(a[-3:2])
print(a[-3:-1])


# In[9]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
names


# In[10]:


data = np.random.randn(7, 4)
data


# In[13]:


data[names == "Bob"]


# In[18]:


data[(names=="Bob") | (names=="Will")][:,[0,-1]]


# In[27]:


data[(names=="Bob") | (names=="Will")][:,[0,-1]]


# In[21]:


print(data)# arr[[rows], [cols]]
# data[[0,-1,3]]
data[:,[0,-1]]


# In[24]:


data[data < 0] = 0
data


# ## Fancy Slicing

# In[30]:


print(data)
print()
print(data[:,[-2,0,-1]])


# In[34]:


print(data)
print()
print(data[0,0])


# In[36]:


a = np.zeros((8,4))
print(a)

for i, v in enumerate(a):
    a[i] = i
a    


# In[38]:


a = np.zeros((8,4))
print(a)

for i in range(len(a)):
    a[i] = i
a    


# In[39]:


a = np.zeros((8,4))
print(a)

for i in range(a.shape[0]):
    a[i] = i
a    


# In[44]:


print(a)
print()
print(a.T)
print()
print(a.transpose())


# In[47]:


a = np.array([[1,2],
             [3,4]])

b = np.array([[5,6],
             [7,8]])

print(a,b ,sep="\n\n", end="\n\n")

print( a * b)


# In[48]:


print( a @ b)


# In[49]:


a.dot(b)


# In[54]:


arr = np.arange(10, 2*2*4+10).reshape((2, 2, 4))
arr


# In[52]:


arr.transpose()


# In[55]:


print(arr)
arr.transpose((1, 0, 2))


# In[57]:


print(arr)
arr.swapaxes(1, 2)


# In[59]:


a = np.arange(3*4).reshape((3,4))
print(a)

a.swapaxes(1,0)


# In[56]:


get_ipython().run_line_magic('pinfo2', 'arr.transpose')


# ## 4.2 Universal Functions: Fast Element-Wise Array Functions

# In[60]:


a = np.array([1,2,-3,4,-5,7,9])
print(np.abs(a))


# In[61]:


a = np.array([1,2,-3,4,-5,7,9])
print(np.fabs(a))


# In[62]:


get_ipython().run_line_magic('pinfo2', 'np.exp')


# In[64]:


a = np.array([1.27, 3.9, 9.2])
f, w = np.modf(a)
print(w,f, sep="\n")


# In[67]:


a = np.array([11,20,25])
np.fmod(a,3)


# In[72]:


a = np.array([1,2,3])
b = np.array([-1,5,7])

np.maximum(a,b)


# In[73]:


a = np.array([1,2,3])
b = np.array([-1,5,7])

np.minimum(a,b)


# In[75]:


a = np.array([1,2,3])
b = np.array([-1,5,7])

np.fmax(a,b)


# # 4.3 Array-Oriented Programming with Arrays

# In[79]:


a = np.arange(3*2).reshape((3,2))
print(a)

print(np.meshgrid(a,a))


# In[80]:


a = np.arange(36)
a % 3 == 0


# In[81]:


a = np.arange(36)
#np.where(condition, true_value, false_value)
np.where(a%3==0, "yes","no")


# # Mathematical and Statistical Methods

# In[83]:


a = np.arange(3*4).reshape((3,4))
print(a)


# In[84]:


np.sum(a)


# In[85]:


a = np.arange(3*4).reshape((3,4))
print(a)
np.sum(a, axis=0)


# In[86]:


a = np.arange(3*4).reshape((3,4))
print(a)
np.sum(a, axis=1)


# In[87]:


a = np.array([1,3,6,8,20,2,3])
np.argmax(a)


# In[88]:


np.argsort(a)


# In[ ]:





# In[ ]:


Linag
Universal function
stack,
in1d, in


# In[ ]:





# In[ ]:




