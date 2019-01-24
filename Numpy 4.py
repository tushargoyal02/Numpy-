#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


start = np.zeros((3,4))
print(start)


# In[5]:


start1 = np.array([1,2,3,4])
print(start1)


# In[7]:


result = start + start1
print(result)


# In[23]:


# .T IS USED TO TRANSPOSE THE ELEMENTS IN AN ARRAY

start2 = np.array([[2,4,6]])
start2 = start2.T
print(start2)


# In[24]:


out1 = start + start2 
print(out1)


# In[27]:


zz = np.array([[0,0],[0,0]])
zz1 = np.array([1,1])
zz2 =1 


# In[29]:


print(zz+zz1)
print()
print(zz+zz2)


# In[ ]:





# In[30]:


from numpy import  arange


# In[31]:


from timeit import time


# In[ ]:




