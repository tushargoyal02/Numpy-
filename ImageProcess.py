#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy import misc


# In[3]:


import matplotlib.pyplot as plt


# In[ ]:





# In[4]:


# THIS PACKAGE IS ONLY AVAILABLE WITH 1.0 PACKAGE NOT WITH 1.2
from skimage import data
#photo_data = misc.imread("/home/tushar/sd-3layers.jpg")


# In[5]:


import imageio
photo_data = imageio.imread("/home/tushar/sd-3layers.jpg")
type(photo_data)


# In[6]:


# using matplotlib
    # we are givving the frame size
plt.figure(figsize=(15,15))


# WE ARE USING (IMSHOW ) FUNCTION TO SHOW THE IMAGE OF THAT FRAME OF THE SCI PACKAGE
plt.imshow(photo_data)


# In[7]:


# TO SEE THE DIMENSION OF THE IMAGE 

print(photo_data.shape)
photo_data.shape

# HERE 3725 IS THE HEIGHT
    #WIDTH IS 4797
        # has THREE layers (3 layer for rgb)


# In[8]:




        # COLOR MAPPING IN PHOTO
    
    #  --- Red show the altitude of geographical data point
    # --- Blue will show the measure of aspect
    # ---- Green will show the slope
    
    


# In[9]:


print(photo_data)


# In[10]:


# to check the size
photo_data.size


# In[11]:


#check maximum and minimum of data value

photo_data.min() , photo_data.max()


# In[12]:


# TO SHOW THE RGB VALUES FOR THE PARTICULAR COLUMN

photo_data[150,250]


# In[13]:


# FOR THE SPECIFIC GREEN VALUE LET INDEX PASS TO IT
photo_data[150,250,1]

    #green value is 35


# In[14]:


# LETS CHANGE THE PIXEL OF THE IMAGE TO WHITE AND LETS SHOW THE IMAGE
photo_data[150,250] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[15]:


photo_data1 = imageio.imread("/home/tushar/sd-3layers.jpg")
photo_data1[100:,:300] =  110
plt.figure(figsize=(10,10))
plt.imshow(photo_data1)


# In[16]:


photo_data = imageio.imread("/home/tushar/sd-3layers.jpg")
print("value of the shape of photo_data are:" , photo_data.shape )

# IN BELOW WE ARE CHECKING THE IMAGE COLOR (255) WITH THE OTHERS SO THAT TO CHANGE IT LATER

low_value_filter =  photo_data < 200
print("shape of low value filter:", low_value_filter.shape)


# In[17]:


# NOW PLOTTING ALL THE IMAGES AND LETTING THE VALUE CHANGE IN THE PIC

plt.figure(figsize=(10,10))
plt.imshow(photo_data)

#setting the value of photo_data array to some different color

photo_data[low_value_filter] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[18]:


np.arange(6)


# CREATING AN RANGE ARRAY OF ROWS AND COLUMNS 
        # WE HAVE CREATED THIS TO SET THE PIXELS TO FULL DENSITY OF THIS NDARRAY
rowArray = np.arange(len(photo_data))
columnArray = rowArray
print(type(rowArray))
print(rowArray)


# In[19]:


#SETTING THE VALUE FOR THE ARRAY = 255 

photo_data[rowArray,columnArray] = 255
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[ ]:





# In[ ]:





# In[30]:


# CREATING THE EUCLID DISTANCE (distance FROM THE CENTER OF CIRCLE to its radius)
    
    
    #setting the number of rows ,column and layeers
    totalRow , totalColumn, totalLayers = photo_data.shape
    print("photo data :",photo_data.shape)
    print(totalRow,totalColumn,totalLayers)


# In[42]:


############
###### -------- [WE WILL BE USING THE OGRID FUNCTION  TO HELP US VECTORISE DISTANCE FROM CENTER]
    
        # OGRID FUNCTION WILL RETURN THE NDARRAY

    X , Y = np.ogrid[:totalRow,:totalColumn]
    print(X,Y)
    
    # HERE X ,Y POINTS ARE USED TO CALCIULATE THE DISTANCE OUTSIDE OF THE RADIUS
    print(X.shape, Y.shape)


# In[ ]:





# In[38]:


# CALCULATING THE CENTER OF THE CIRCLE
     centerRow , centerColumn = totalRow/2 ,totalColumn/2
     print(centerRow,centerColumn)


# In[40]:


print(X - centerRow)


# In[43]:


print(Y-centerColumn)


# In[45]:




# DISTANCE FROM CENTER  X square + Y-square
distance_center = (X-centerRow)**2 + (Y-centerColumn)**2


# RADIUS FOR THE CIRCLE   r^2 (x^2 + y^2 = r^2)
radius = (totalRow / 2)**2


# IT WILL CHECK THE BOOLEAN VALUE FOR THE GIVEN VALUES
circular_mask = (distance_center > radius)

print(circular_mask)


# 

# In[48]:


# setting the rows and column for the given rows and column (True and False value can be used to find value in or outside 
# the circle)

print(circular_mask[1500:1700,2000:2200])


# In[50]:


# 1 loading image from the path
    # 2 providing the ndarray  to the circular mask [False values are given hence the True values are set to black]
        # 3 setting the size
            # 4 showing the image

photo_data = imageio.imread('/home/tushar/sd-3layers.jpg')
photo_data[circular_mask] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[52]:


# GETTING MUCH BETTER MASK
X , Y = np.ogrid[:totalRow,:totalColumn]

# getting all values for 
halfUpper = X < centerRow   #massk for all values row  above


# WE are doing THE LOGICAL AND OPERATION TO COMBINE THE TWO FILTER VALUES
half_upper_mask = np.logical_and(halfUpper,circular_mask)


# In[55]:


photo_data = imageio.imread("/home/tushar/sd-3layers.jpg")
photo_data[half_upper_mask] = 255
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[59]:


import random
photo_data111 =  imageio.imread("/home/tushar/sd-3layers.jpg")
photo_data111[half_upper_mask] =  random.randint(200,255)
plt.figure(figsize=(10,10))
plt.imshow(photo_data111)


# In[65]:


photo_data = imageio.imread("/home/tushar/sd-3layers.jpg")
red_mask = photo_data[:,:,0] < 150
photo_data[red_mask] = 0 
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[71]:


photo_data = imageio.imread("/home/tushar/sd-3layers.jpg")
green_mask = photo_data[:,:,1] > 100 
photo_data[green_mask] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[72]:


photo_data = imageio.imread("/home/tushar/sd-3layers.jpg")
blue_mask = photo_data[:,:,2] > 120 
photo_data[blue_mask] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[77]:


# COMBINING ALL THREE MASK ARE :
final_mask = np.logical_and(red_mask,green_mask,blue_mask)
photo_data[final_mask] = 0
plt.figure(figsize=(10,15))
plt.imshow(photo_data)


# In[ ]:




