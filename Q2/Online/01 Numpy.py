#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = range(1000000)
get_ipython().run_line_magic('time', 'for i in range(1,10): [x*2 for x in list1]')


# In[2]:


import numpy as np
list2 = np.arange(1000000)
get_ipython().run_line_magic('time', 'list2 * 2')


# In[3]:


z = np.zeros((4,4))
print(z)


# In[4]:


z = np.ones((4,4))
print(z)


# In[5]:


z = np.empty((4,4))
print(z)
# Data Can be anything other


# In[6]:


list1 = [1,4,5,7]
np.array(list1)


# In[7]:


np.arange(1,100000,100)


# In[9]:


z.shape


# In[12]:


z.reshape((2,2,2,2))


# In[13]:


z.ndim


# In[14]:


a = np.random.randn((10))
b = np.random.randn((10))
print(a,b)


# In[15]:


a+b


# In[16]:


a-b


# In[17]:


a*b


# In[18]:


a/b


# In[19]:


a**2


# In[20]:


a>0


# In[21]:


a[a>0]


# In[22]:


x=np.array([1,7,9,8,5])
x[4]


# In[23]:


x[x>5]


# In[24]:


x[[2,1]]


# In[26]:


x=np.random.randn(10,10)


# In[27]:


x[0]


# In[28]:


x[1::2]
#Odd Rows


# In[29]:


x[::,0:4]


# In[30]:


#Making a square with ones in border and zeroes in center
square = np.ones((5,5))
square[1:-1,1:-1]=0


# In[31]:


square


# In[32]:


x=np.array([10,9,8,6,11])
np.sqrt(x)


# In[33]:


np.power(x,2)


# In[34]:


y=np.array([7,11,3,8,10])
np.maximum(x,y)


# In[36]:


np.max(x)


# In[37]:


x=np.array([0,-1,10000,111,22121])
np.where(x<=0,25000,x)


# In[38]:


np.where(x<=0,25000,"NOT OK")


# In[39]:


print(True+True)


# In[40]:


x=np.array([10,9,7,10,7])
x.mean()


# In[42]:


x.cumsum()


# In[46]:


y = x>8
print(y)


# In[44]:


y.sum()


# In[45]:


y.any()


# In[47]:


y.all()


# In[49]:


x.sort()
x


# # File I/O

# In[21]:


x=[1,4,5,7,1]
y=[8,7,9]
np.savez('testx',x=x,y=y)
loading = np.load('testx.npz')
loading
loading['y']


# # LA

# In[25]:


x=np.random.randn(3,2)
y=np.random.randn(2,3)
x


# In[26]:


y


# In[27]:


x.dot(y)


# In[28]:


x.transpose()


# # Pseudo Random Numbers

# In[30]:


np.random.seed(7)
np.random.normal(size=(3,3))


# In[32]:


x=np.random.randn(4,5)
x.reshape(2,2,5)


# In[33]:


x.ravel()


# In[34]:


x.flatten()


# In[35]:


x = np.arange(100)


# In[36]:


x


# In[43]:


x.reshape(50,2,order='F')


# In[44]:


x.reshape(50,2,order='C')


# # Concatenate

# In[54]:


arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[3,2,1],[7,6,5]])
np.concatenate((arr1,arr2),axis=0)


# In[56]:


d = np.array([1,4,5,6,7,9,1,4])
np.split(d,[2,5])


# In[58]:


d = np.array([[1,4,5,6],[7,9,1,4]])
np.split(d,[2,5],axis=1)


# In[59]:


d=np.array([1,5,7,8])


# In[62]:


np.repeat(d,2)


# In[65]:


np.tile(d,2)


# In[ ]:




