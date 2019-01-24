#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


# python assigns datatype by itself so .dtype is used to check the datatype 
ex1 = np.array([11,12])
print(ex1.dtype)


# In[9]:


# to forcefully gives the data-type

ex2 = np.array([1.0,2.0,3.0], dtype=np.int64)
print(ex2.dtype)


# In[15]:


# ARITHMETIC OPERATIONS

x = np.array([[111,112],[121,122]],dtype=np.int)
y= np.array([[211.1,212.1],[221.1,222.1]],dtype=np.float64)
print(x)
print(y)


# In[19]:


print(x+y)
print()
print()
print(np.add(x,y))


# In[20]:


print(np.subtract(x,y))


# In[ ]:




