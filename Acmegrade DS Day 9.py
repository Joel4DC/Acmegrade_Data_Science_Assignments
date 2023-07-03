#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day 9


# In[2]:


#1. Extract data from the given SalaryGender CSV file and store the data from each column in a separate NumPy array.


# In[39]:


import numpy as np
import pandas as pd


# In[40]:


df=pd.read_csv("D:\Study Material\Data Science\Acmegrade\Day 9\CS 15 Ans -Data Transformation-1\SalaryGender.csv")


# In[41]:


df.head()


# In[42]:


salary = np.array(df['Salary'])
salary


gender = np.array(df['Gender'])
gender


age = np.array(df['Age'])
age


phd = np.array(df['PhD'])
phd


# In[43]:


#2. Find:
#2a The number of men with PhD,
#2B The number of women with PhD.


# In[44]:


salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
phd = np.array(df['PhD'])
age = np.array(df['Age'])

men_count = 0
women_count = 0

for i in range(0, 100):
    if gender[i] == 1 and phd[i] == 1:
        men_count +=1
    if gender[i] == 0 and phd[i] == 1:
        women_count +=1

print('Men Count', men_count)
print('Woman Count',women_count)


# In[45]:


#3. Use SalaryGender CSV file. 
#Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD.


# In[46]:


salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
phd = np.array(df['PhD'])
age = np.array(df['Age'])

frame = pd.DataFrame()
frame["Age"] = age
frame["PhD"] = phd

for i in range(0, 100):
    if frame.loc[i]["PhD"] == 0:
        frame = frame.drop(i)
print('Number of records',len(frame))
print(frame)


# In[47]:


#4. Calculate the total number of people who have a PhD degree from SalaryGender CSV file.


# In[48]:


phdcount=0

for i in range(0, 100):
    if df.iloc[i]['PhD'] == 1:
        phdcount=phdcount+1

        
print('PhD Count:',phdcount)


# In[49]:


#5. How do you Count The Number Of Times Each Value Appears In An Array Of Integers?


# In[50]:


arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
print(np.bincount(arr))


# In[51]:


#6. Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements greater than 5.


# In[52]:


import numpy as np
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
print('Our array is:' )
print(x)
print('\n')


# In[53]:


print(x[x > 5])


# In[54]:


#7. Create a numpy array having NaN (Not a Number) and print it.


# In[55]:


a = np.array([np.nan, 1,2,np.nan,3,4,5])
print(a)
print(a[~np.isnan(a)])


# In[56]:


#8. Create a 10x10 array with random values and find the minimum and maximum values.


# In[57]:


Z = np.random.random((10,10))
print (pd.DataFrame(Z))


Zmin, Zmax = Z.min(), Z.max()
print ('Min and Max Values')
print(Zmin, Zmax)


# In[58]:


#9. Create a random vector of size 30 and find the mean value.


# In[59]:


Z = np.random.random(30)
m = Z.mean()
print(m)


# In[60]:


#10. Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9


# In[61]:


Z = np.arange(11)
print ('Array')
print (Z)

Z[(3 < Z) & (Z <= 8)] *= -1
print ('Negeted Array')
print(Z)


# In[62]:


#11. Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column.


# In[63]:


Z = np.random.randint(0,10,(3,3))
print(Z)
print ()

print(Z[Z[:,1].argsort()])


# In[64]:


#12. Create a four dimensions array (2,2,2,2) get sum over the last two axis at once.


# In[65]:


A = np.random.randint(0,10,(2,2,2,2))
print ('Array')
print (A)

sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print ('Result')
print(sum)


# In[66]:


#13. Create a random array ( 5,5) and swap two rows of an array.


# In[67]:


A = np.arange(25).reshape(5,5)
print ('Random Array')
print (A)
# First row assigned to Zeroth row and zero row assigned to first row

A[[0,1]] = A[[1,0]]
print ()
print ('Swapped Array')
print(A)


# In[68]:


#Completed.

