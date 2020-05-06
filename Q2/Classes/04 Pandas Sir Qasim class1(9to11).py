#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv("./data/abc.csv", encoding='cp1252') #utf-8
df.head(10)


# In[6]:


df = pd.read_excel("./data/abc.xlsx")
df.head(10)


# In[7]:


df = pd.read_excel("./data/abc.xlsx", sheet_name="Sheet1")
df.head(10)


# In[8]:


df = pd.read_excel("./data/abc.xlsx", sheet_name=0) # sheetName/sheetIndexNo
df.head(10)


# In[18]:


df = pd.read_excel("./data/abc.xlsx", sheet_name=0, usecols=["A","C"]) # sheetName/sheetIndexNo
df.head(10)


# In[9]:


df = pd.read_html("https://www.w3schools.com/html/html_tables.asp")
df


# In[10]:


df = pd.read_html("https://www.w3schools.com/html/html_tables.asp")[0]
df


# In[ ]:





# In[13]:


df = pd.read_html("https://www.w3schools.com/html/html_tables.asp")
df[0]


# In[14]:


df = pd.read_json("https://api.github.com/users/hadley/orgs")
df.head()


# In[19]:


df = pd.read_json("https://api.github.com/users/hadley/orgs",)
df.head()


# In[23]:


type(df)


# In[25]:


type(df.login)


# In[20]:


df.to_excel("data/online_data.xlsx", index=False)


# In[21]:


#df.to_csv("data/online_data.csv", index=False)


# # Tabula-py (for pdf)

# In[15]:


get_ipython().run_line_magic('pinfo2', 'pd.read_feather')


# # Series

# In[26]:


df.login


# In[27]:


df.login.index


# In[28]:


df.login.values


# In[29]:


obj = pd.Series([4, 7, -5, 3])
obj


# In[30]:


obj2 = pd.Series([1,2,3,4], index=['A','B',"C",'D'])
obj2


# In[31]:


obj3 = pd.Series([7,8,9,10], index=['A','D','E','F'])
obj3


# In[35]:


obj3.index


# In[34]:


print(obj2, obj3, sep="\n\n")
obj2 + obj3


# In[37]:


date_range = pd.date_range('2020-01-01', '2020-05-03') #YYYY-MM-DD
date_range


# In[38]:


date_range[-1]


# In[39]:


date_range = pd.date_range('2020-01-01', periods=5) #YYYY-MM-DD
date_range


# In[40]:


date_range = pd.date_range('2020-01-01', '2020-05-03', freq='M') #YYYY-MM-DD
date_range


# In[41]:


date_range = pd.date_range('2020-01-01', periods=5, freq='5H') #YYYY-MM-DD
date_range


# In[44]:


obj2 = pd.Series([1,2,3,4], index=['A','B',"C",'D'])
print(obj2)


# In[46]:


print(obj2)
obj2['C']


# In[48]:


print(obj2)
obj2['C'] = 10
print(obj2)


# In[49]:


print(obj2)
obj2[['D',"B"]]


# In[ ]:




