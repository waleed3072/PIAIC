#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui as pg


# In[53]:


x,y=pg.position()


# In[54]:


delay=3
pg.moveTo(x,y,delay)
pg.click()
pg.moveTo(x+291,y,delay)
pg.click()


# In[79]:


pg.keyDown('win')
pg.sleep(0.5)
pg.keyDown('r')
pg.keyUp('r')
pg.keyUp('win')
pg.write('cmd')
pg.hotkey('shift','ctrl','enter')


# In[86]:


pg.keyDown('win')
pg.sleep(0.5)
pg.keyDown('s')
pg.keyUp('s')
pg.keyUp('win')
pg.write('Neo')
pg.hotkey('enter')


# In[90]:


pg.hotkey('win','r')


# In[ ]:




