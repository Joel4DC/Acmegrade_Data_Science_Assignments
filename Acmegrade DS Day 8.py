#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day 8


# In[2]:


#1. Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array. 


# In[3]:


import numpy as np
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a = np.array(l)
print("One-dimensional NumPy array: ",a)


# In[4]:


#2.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.


# In[5]:


x =  np.arange(2, 11).reshape(3,3)
print(x)


# In[6]:


#3. Write a NumPy program to create a null vector of size 10 and update sixth value to 11.


# In[7]:


x = np.zeros(10)
print(x)
print("Update sixth value to 11")
x[6] = 11
print(x)


# In[8]:


#4. Write a NumPy program to create an array with values ranging from 12 to 38.


# In[9]:


x = np.arange(12, 38)
print(x)


# In[10]:


#5. Write a NumPy program to reverse an array (first element becomes last).


# In[11]:


x = np.arange(12, 38)
print("Original array:")
print(x)
print("Reverse array:")
x = x[::-1]
print(x)


# In[12]:


#6. Write a NumPy program to convert an array to a float type.


# In[13]:


a = [1, 2, 3, 4]
print("Original array")
print(a)
x = np.asfarray(a)
print("Array converted to a float type:")
print(x)


# In[14]:


#7. Write a NumPy program to create a 2d array with 1 on the border and 0 inside.


# In[15]:


x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)


# In[16]:


#8. Write a NumPy program to add a border (filled with 0's) around an existing array.


# In[17]:


x = np.ones((3,3))
print("Original array:")
print(x)
print("0 on the border and 1 inside in the array")
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)


# In[18]:


#9. Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.  


# In[19]:


x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


# In[20]:


#10. Write a NumPy program to convert a list and tuple into arrays.


# In[21]:


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
print(np.asarray(my_list))
my_tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
print(np.asarray(my_tuple))


# In[22]:


#11. Write a NumPy program to append values to the end of an array.


# In[23]:


x = [10, 20, 30]
print("Original array:")
print(x)
x = np.append(x, [[40, 50, 60], [70, 80, 90]])
print("After append values to the end of the array:")
print(x)


# In[24]:


#12. Write a NumPy program to create an empty and a full array. 


# In[26]:


# Create an empty array
x = np.empty((3,4))
print(x)
# Create a full array
y = np.full((3,3),6)
print(y)


# In[27]:


#13. Write a NumPy program to convert the values of Centigrade degrees into Fahrenheit degrees.
#Centigrade values are stored into a NumPy array. 


# In[28]:


fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:") 
print(5*F/9 - 5*32/9)


# In[29]:


#14. Write a NumPy program to find the real and imaginary parts of an array of complex numbers.


# In[30]:


x = np.sqrt([1+0j])
y = np.sqrt([0+1j])
print("Original array:x ",x)
print("Original array:y ",y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag)


# In[ ]:


#Completed.

