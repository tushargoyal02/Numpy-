#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr =  10 * np.random.random([3,3])
print(arr)


# In[3]:


print(arr.mean())


# In[4]:


# MEAN FOR THE ROWS

print(arr.mean(axis = 1))


# In[6]:


# MEAN FOR THE COLUMNS
 print(arr.mean())


# In[9]:


# TO CALCULATE THE MEDIANS OF THE FILE

print(np.median(arr ,axis=1))


# In[12]:


unsorted = np.random.random(10)
print(unsorted)


# In[16]:


# SORTHING THE VALUES

unsorted.sort()
print(unsorted)


# In[19]:


# TO GET THE UNIQUE VALUES
arr3 = np.array([1,2,3,1,1,2,456,55])
print(np.unique(arr3))


# In[21]:


s1 = np.array(["hii","chair","bulb"])
s2 = np.array(["baba","chair","lili"])
print(s1,s2)


# In[25]:


print(np.intersect1d(s1,s2))
print()
print(np.union1d(s1,s2))


# In[26]:


# TO GET VALUES IN S1 BUT NOT IN S2
print(np.setdiff1d(s1,s2))


# In[28]:


# ELEMENTS WHICH ARE IN S1 AND S2 TOO (TAKE ELEMENT 1 OF ARRAY AND COMPARES WITH ALL VALUE IN 2 ARRAY)
print(np.in1d(s1,s2))


# In[ ]:




