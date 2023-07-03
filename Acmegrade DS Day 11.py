#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Day 11


# In[16]:


#1. You are given a dataset, containing the number of hurricanes (Hurricanes.csv) occurring in the United States along the coast of the Atlantic. 
#Load the data from the dataset into your program and plot a Bar Graph of the data, 
#taking the Year as the x-axis and the number of hurricanes occurring as the Y-axis.


# In[92]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


# In[93]:


hurr = pd.read_csv('D:\Study Material\Data Science\Acmegrade\Day 11\CS 17 Ans -Data Transformation-3\Hurricanes.csv', delimiter=',')
hurr.head()


# In[94]:


plt.rcParams["figure.figsize"] = (20,10)
plt.bar(hurr["Year"], hurr["Hurricanes"])
plt.show()


# In[95]:


#2. The dataset given, records data of city temperatures over the years’ 2014 and 2015.
#Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.


# In[96]:


temp = pd.read_csv("D:\Study Material\Data Science\Acmegrade\Day 11\CS 17 Ans -Data Transformation-3\CityTemps.csv", delimiter=',')
temp.head()


# In[97]:


plt.hist([temp["San Francisco"],temp["Moscow"]], bins= [-10,-5,0,5,10,15,20],rwidth= 1, label= ["SF", "Moscow"] )
plt.legend()


# In[98]:


#3.1 Load the Data set sample-salesv2.csv , then display top 5 records.


# In[99]:


sales=pd.read_csv("D:\Study Material\Data Science\Acmegrade\Day 11\CS 17 Ans -Data Transformation-3\sample-salesv2.csv",parse_dates=['date'])
display(sales.head())


# In[100]:


#3.2 Use the Describe statement and describe the column – Unit Price.


# In[101]:


print(sales['unit price'].describe())


# In[102]:


#3.3 Extract the columns / create  a data frame customers, with columns Name, Net_price. 
#Do the group by based on column name 


# In[103]:


customers = sales[['name','net_price','date']]
customers


# In[104]:


customer_group = customers.groupby('name')
print(customer_group.size())


# In[105]:


#3.4 Create bar graph, customer by Sales ( x- axis – Customer , y-axis – Sales).


# In[106]:


sales_totals = customer_group.sum()
my_plot = sales_totals.plot(kind='bar')
plt.show()


# In[107]:


#Let the x axis data points and y axis data points are:
#x = [1,2,3,4]
#y = [20, 21, 20.5, 20.8]


# In[108]:


#4.1 Draw a Simple plot.


# In[109]:


x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
plt.plot(x, y)
plt.show()


# In[110]:


#4.2 Configure the line and markers in simple plot.


# In[111]:


x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

plt.plot(x, y, linestyle="dashed", marker="o", color="green")
plt.show()


# In[112]:


#4.3 configure the axes.


# In[113]:


#define  data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")


#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])


#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#show plot
plt.show()


# In[114]:


#4.4 Give title of Graph & labels of x axis and y axis.


# In[127]:


x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#configure  X axes

plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes

plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

#show plot
plt.show()


# In[128]:


#4.5 Give error bar if y_error = [0.12, 0.13, 0.2, 0.1].


# In[116]:


#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#error data
y_error = [0.12, 0.13, 0.2, 0.1]

#plot data

plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#plot only errorbars

plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="blue")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

#show plot
plt.show()


# In[117]:


#4.6 define width, height as figsize=(4,5) DPI and adjust plot dpi=10.


# In[118]:


#define plot size in inches (width, height) & resolution(DPI)
fig = plt.figure(figsize=(4, 5), dpi=100)

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#error data
y_error = [0.12, 0.13, 0.2, 0.1]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#plot only errorbars
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="blue")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

#adjust plot
plt.subplots_adjust(left=0.18)

#show plot
plt.show()


# In[119]:


#4.7 Give a font size of 14.


# In[120]:


#define plot size in inches (width, height) & resolution(DPI)

fig = plt.figure(figsize=(4, 5), dpi=100)

#define font size

plt.rc("font", size=14)

#define some data

x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

plt.plot (x,y)


# In[121]:


#4.8 Draw a scatter graph of any 50 random values of x and y axis.


# In[122]:


N = 50

x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)

area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.show()


# In[123]:


#4.9 Create a dataframe from following data:

#'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
#'female': [0, 1, 1, 0, 1],
#'age': [42, 52, 36, 24, 73],
#'preTestScore': [4, 24, 31, 2, 3],
#'postTestScore': [25, 94, 57, 62, 70]

#Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age.


# In[124]:


raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])

print(df.head())

plt.scatter(df.preTestScore, df.postTestScore, s=df.age)


# In[125]:


#4.10 Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore with the size = 300
#and the color determined by sex.


# In[126]:


plt.scatter(df.preTestScore, df.postTestScore, s=300, c=df.female)


# In[ ]:


#Completed.

