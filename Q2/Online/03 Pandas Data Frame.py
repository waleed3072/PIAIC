#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
pd.DataFrame({'apple':['5'],'Banana':['6Kg'],'Mangoes':['10kg']})


# In[8]:


pd.DataFrame({'apple':['5','5','5','5'],
              'Banana':['6Kg','6Kg','6Kg','6Kg'],
              'Mangoes':['10kg','10kg','10kg','10kg']},
             columns=['Banana',"apple",'Mangoes'])


# In[ ]:




