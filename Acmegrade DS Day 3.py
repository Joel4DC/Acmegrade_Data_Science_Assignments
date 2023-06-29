#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Acmegrade Assignment


# In[2]:


#Day 3


# In[3]:


#1. Write a Python program to count the number 4 in a given list.


# In[6]:


def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count


print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))


# In[7]:


#2. Write a Python program to test whether a passed letter is a vowel or not.


# In[8]:


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


print(is_vowel('c'))
print(is_vowel('e'))


# In[9]:


#3. Write a Python program to check whether a specified value is contained in a group of values.  


# In[10]:


def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False

print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))


# In[11]:


#4. Write a Python program to create a histogram from a given list of integers.


# In[14]:


def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '@'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5]) 


# In[ ]:


#5. Write a Python program to concatenate all elements in a list into a string and return it.


# In[13]:


def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))


# In[15]:


#6. Write a Python program that will accept the base and height of a triangle and compute the area. 


# In[16]:


b = int(input("Input the base : "))
h = int(input("Input the height : "))
area = b*h/2

print("area = ", area)


# In[17]:


#7. Write a Python program to sum of three given integers. 
# However, if two values are equal sum will be zero.


# In[18]:


def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3)) 
print(sum(5, 4, 3)) 


# In[19]:


#8. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


# In[20]:


def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

print(sum(10, 6))
print(sum(10, 2))
print(sum(10, 12))


# In[21]:


#9. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.  


# In[22]:


def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))


# In[23]:


#10. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).


# In[24]:


import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)


# In[ ]:


#Completed

