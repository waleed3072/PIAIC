#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
pd.Series(['123123.12',3,21.3,12,.3,21.,3.12,3123])


# In[7]:


sales = pd.Series([100,200,100,400])
sales.index


# In[8]:


sales = pd.Series([100,200,100,400],index = ['a','b','c','d'])
sales.index


# In[9]:


sales


# In[11]:


sales = pd.Series([100,200,100,400],index = ['a','b','c','d'])
sales


# In[13]:


pd.array([1,2,3,4,5,'6'])


# In[6]:


# movies = [("Star Wars",1970),("Jedi",2020),("Clone Wars",2002),("Avengers",2032),("Messi",2010),("Ronaldo",2011),("Gandhi",2000),("Goal",2003),]
# [title[0] for title in movies if title[1] >= 2000]
import numpy as np
get_ipython().run_line_magic('time', 'range(1000000)')
get_ipython().run_line_magic('time', 'np.arange(1000000)')
get_ipython().run_line_magic('time', 'pd.Series(1000000)')


# In[4]:


import pandas
pandas.Series([1,3,4,5,6,5,45,6,43,534,534],index=range(6,17),name="Random Ints")


# In[5]:


x = pandas.Series([1,3,4,5,6,5,45,6,43,534,534],index=range(6,17),name="Random Ints")
x[[6,7,8]]


# In[12]:


6 in x


# In[13]:


4 in x.values


# In[14]:


continents = {'Sindh':30009,'Punjab':50009,'Balochistan':20009,'KPK':60009,'Gilgit':10009}
x = pandas.Series(continents,index=['Sindh','Punjab','Balochistan','KPK','Gilgit'])
x


# In[15]:


continents = {'Sindh':30009,'Punjab':50009,'Balochistan':20009,'KPK':60009,'Gilgit':10009}
x = pandas.Series(continents,index=['Punjab','Sindh','Balochistan','KPK','Gilgit'])
x


# In[ ]:




