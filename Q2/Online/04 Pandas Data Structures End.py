#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
frame = pd.DataFrame(np.random.randn(4,3), columns=list('bde'),
                            index=['Utah','Ohio','Texas','Oregon'])
frame


# In[8]:


np.abs(frame)


# In[9]:


frame['d'].min()


# In[10]:


func = lambda x: x.max() - x.min()
func(frame)


# In[12]:


frame.apply(func)


# In[13]:


frame.apply(func,axis=1)


# In[14]:


frame.sort_index(axis=1,ascending=True)


# In[15]:


frame.sort_index(axis=1,ascending=False)


# In[16]:


frame.sort_index(axis=0,ascending=False)


# In[17]:


frame.sort_index(axis=0,ascending=True)


# In[18]:


frame.sort_values(by='b')


# In[19]:


frame.sort_values(by='b',ascending=False)


# In[21]:


frame.rank()


# In[22]:


frame.rank(axis=1)


# In[23]:


frame.sum()


# In[26]:


frame.sum(axis="columns")


# In[27]:


frame.mean()


# In[28]:


frame['b'] = None


# In[29]:


frame


# In[33]:


frame.mean()


# In[34]:


frame.mean(axis=1)


# In[36]:


frame.mean(axis=1,skipna=False)


# In[37]:


frame.mean(axis=1,skipna=True)


# In[45]:


frame['b'] = np.random.randn(4)


# In[46]:


frame


# In[51]:


frame['a'] = ""


# In[52]:


frame


# In[53]:


frame.pop('a')


# In[54]:


frame


# In[55]:


frame['b']['Utah'] = np.nan


# In[56]:


frame


# In[57]:


frame.mean(axis=1,skipna=True)


# In[58]:


frame.mean(axis=1,skipna=False)


# In[63]:


frame.loc[['Utah','Ohio'],['b','d']]


# In[64]:


frame.iloc[[2,3],[0,1]]


# In[67]:


frame.iloc[:,:]


# In[68]:


frame.iloc[:,:2]


# In[70]:


frame.drop('b',axis=1)


# In[74]:


frame.drop('b',axis=1,inplace=True)


# In[75]:


frame


# In[76]:


frame['b'] = np.random.randn(4)


# In[77]:


frame


# In[78]:


frame.drop('Utah',axis=0)


# In[80]:


frame = pd.Series(['blue','green','red'],index=[0,3,6])
frame


# In[88]:


frame.reindex(range(9),method='ffill')


# In[87]:


frame.reindex(range(6),method='ffill')


# In[89]:


frame.reindex(range(12),method='ffill')


# In[90]:


# Reindex Creates new rows. ANd 'ffill' fills new rows with previous values
frame.reindex(range(12))


# In[93]:


frame = pd.DataFrame(np.random.randn(4,3), columns=list('bde'),
                            index=range(4))
frame


# In[94]:


frame.reindex(range(12))


# In[95]:


frame.reindex(range(12),method='ffill')


# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
data_df = pd.DataFrame( np.arange(16).reshape((4,4)),
                      index = ['Ohio','Colorado','Utah','New York'],
                      columns=['One','Two','Three','Four'])
# print(data_df,'\n')
# df2 = data_df[['One','Three']]
# print(df2)
# print( data_df[2:] )
print(data_df['One'])

# Conditional Selection
# print(data_df[data_df['Three']]>5)
# print(data_df,'\n')

# df2 = data_df[data_df['Three']]>5
# print(df2)
# print(data_df[data_df['Three']]>5)


# In[ ]:




