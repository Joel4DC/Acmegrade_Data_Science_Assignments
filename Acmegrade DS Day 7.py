#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Day 7


# In[19]:


#1.Write a NumPy program to get the numpy version and show numpy build configuration.  


# In[20]:


import numpy as np
print(np.__version__)
print(np.show_config())


# In[21]:


#2. Write a NumPy program to  get help on the add function.


# In[22]:


print(np.info(np.add))


# In[23]:


#3. Write a NumPy program to test whether none of the elements of a given array is zero.


# In[24]:


x = np.array([1, 2, 3, 4])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))


# In[25]:


x = np.array([0, 1, 2, 3])

print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))


# In[26]:


#4. Write a NumPy program to test whether any of the elements of a given array is non-zero.


# In[27]:


x = np.array([1, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))


# In[28]:


x = np.array([0, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))


# In[29]:


#5. Write a NumPy program to test a given array element-wise for finiteness 
#(not infinity or not a Number).


# In[30]:


a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))


# In[31]:


#6. Write a NumPy program to test element-wise for positive or negative infinity.


# In[32]:


a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for positive or negative infinity:")
print(np.isinf(a))


# In[33]:


#7. Write a NumPy program to test element-wise for NaN of a given array.


# In[34]:


a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for NaN:")
print(np.isnan(a))


# In[35]:


#8. Write a NumPy program to test element-wise for complex number, real number of a given array. 
#Also test whether a given number is a scalar type or not.


# In[37]:


a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))


# In[38]:


#9. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) 
#of two given arrays.  


# In[39]:


x = np.array([3, 5])
y = np.array([2, 5])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x, y))
print("Comparison - greater_equal")
print(np.greater_equal(x, y))
print("Comparison - less")
print(np.less(x, y))
print("Comparison - less_equal")
print(np.less_equal(x, y))


# In[40]:


#11. Write a NumPy program to create an array with the values 1, 7, 13, 105 
#and determine the size of the memory occupied by the array.


# In[41]:


X = np.array([1, 7, 13, 105])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))


# In[42]:


#12. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.


# In[43]:


array=np.zeros(10)
print("An array of 10 zeros:")
print(array)
array=np.ones(10)
print("An array of 10 ones:")
print(array)
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)


# In[44]:


#13. Write a NumPy program to create an array of the integers from 30 to70.


# In[46]:


array=np.arange(30,71)
print("Array of the integers from 30 to70")
print(array)


# In[47]:


#14. Write a NumPy program to create an array of all the even integers from 30 to 70.


# In[48]:


import numpy as np
array=np.arange(30,71,2)
print("Array of all the even integers from 30 to 70")
print(array)


# In[ ]:


#Completed

