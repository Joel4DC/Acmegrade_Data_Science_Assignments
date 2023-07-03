#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day 6


# In[2]:


#1. What is the output of the following code?


# In[3]:


nums = set([1,1,2,3,3,3,4,4])
print(len(nums))


# In[4]:


#2. What will be the output?


# In[5]:


d = {"john":40, "peter":45}
print(list(d.keys()))


# In[6]:


#3. Write a for loop that prints all elements of a list and their position in the list.


# In[7]:


a = [4,7,3,2,5,9]
for item in a:
    print(str(item) + " is at position " + str(a.index(item) + 1))


# In[8]:


#4. Please write a program which accepts a string from console and print the characters that have even indexes.


# In[11]:


s=input("Enter an alphanumeric string which wil contain alternate alphabates and numbers: ")
s = s[::2]
print(s)


# In[12]:


#5. Please write a program which accepts a string from console and print it in reverse order.


# In[18]:


s=input("Enter string which you want to reverse")
s = s[::-1]
print(s)


# In[19]:


#6. Please write a program which count and print the numbers of each character in a string input by console


# In[24]:


dic = {}
s= input('Enter string')
for s in s:
    dic[s] = dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))


# In[ ]:


#7. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
#write a program to make a list whose elements are intersection of the above given lists.


# In[25]:


set1={1,3,6,78,35,55}
set2={12,24,35,24,88,120,155}
set1 &= set2
li=list(set1)
print(li)


# In[26]:


#8. Write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].


# In[27]:


li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)


# In[28]:


#9. Write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].


# In[29]:


li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)


# In[30]:


#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).


# In[32]:


n=int(input("Enter a number"))
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)


# In[33]:


#Completed


# In[ ]:




