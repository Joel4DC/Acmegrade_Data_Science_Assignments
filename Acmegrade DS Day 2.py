#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Acmegrade Assignment


# In[ ]:


#Day 2


# In[ ]:


#1. Write a Python program to get the Python version you are using.  


# In[3]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[2]:


#2. Write a Python program to display the current date and time.


# In[ ]:


#i


# In[1]:


import datetime
x = datetime.datetime.now()
print(x)


# In[3]:


#ii


# In[4]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[5]:


#3. Write a Python program which accepts the radius of a circle from the user and compute the area. 


# In[8]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[9]:


#4. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.


# In[10]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[13]:


#5. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers


# In[ ]:


#i


# In[12]:


values = input("Input some comma separated numbers : ")
list1 = values.split(",")
tuple1 = tuple(list1)
print('List : ',list1)
print ('Tuple : ',tuple1)


# In[14]:


#ii


# In[20]:


txt="hello, my name is Peter, I am from UK"
x = txt.split(",")
print(x)


# In[21]:


#iii


# In[28]:


txt="apple#banana#cherry#orange"
x = txt.split("#",2)
print(x)


# In[29]:


#6. Write a Python program to accept a filename from the user and print the extension of that. 


# In[33]:


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


# In[34]:


#7. Write a Python program to display the first and last colors from the following list.  


# In[38]:


color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))


# In[39]:


#8. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 


# In[41]:


a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)


# In[42]:


#9. Write a Python program to get the volume of a sphere with radius 6.


# In[43]:


pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# In[44]:


#10. Write a Python program to convert seconds to day, hour, minutes and seconds.


# In[46]:


time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d days :%d hours:%d minutes:%d seconds" % (day, hour, minutes, seconds))


# In[ ]:


#Complete

