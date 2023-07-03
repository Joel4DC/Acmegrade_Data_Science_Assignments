#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day 12


# In[2]:


#Business challenge/requirement

#BigMart is one of the biggest retailer of Europe and has operations across multiple countries.
#You are a data analyst in IT team of BigMart.
#Invoice and SKU wise Sales Data for Year 2011 is shared with you.
#You need to prepare meaningful charts to show case the various sales trends for 2011 to top management.


# In[3]:


#Key issues

#Data should be displayed pictorially to capture the attention of top management.


# In[4]:


#Data volume
# Approx 500K records – file BigMartSalesData.csv


# In[5]:


#Business benefits

#This exercise is an annual exercise and BigMart makes important investment decision based on trends.


# In[6]:


#Approach to Solve

#You have to use fundamentals of Matplotlib and plot following 4 chart/graph.


# In[7]:


#1.Plot Total Sales Per Month for Year 2011.
#How the total sales have increased over months in Year 2011.
#Which month has lowest Sales?


# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)


# In[10]:


sales_data=pd.read_csv("D:\Study Material\Data Science\Acmegrade\Day 12\CS 18 Ans -Data Transformation-4\BigMartSalesData.csv")
sales_data.head()


# In[11]:


print(sales_data.info())


# In[12]:


# Get Sales for the Year 2011


# In[14]:


print (" Getting Sales Data for Year 2011")
sales_2011 = sales_data[sales_data['Year'] == 2011]


# In[15]:


sales_2011_month = sales_2011.groupby('Month').sum()['Amount']
print(sales_2011_month)


# In[16]:


# Simply Plot the Sales Data for 2011,
#X Axis Sales for each month,
#Y -Axis Month Number.


# In[17]:


plt.plot(sales_2011_month.index,sales_2011_month.values)

plt.xlabel("Sales in Euro")
plt.ylabel("Month Number")
plt.title("Sales Per Month in Year 2011")
plt.show()


# In[18]:


# Save the Plot Locally


# In[19]:


plt.savefig("Year2011MonthWiseSales")


# In[20]:


#2. Plot Total Sales Per Month for Year 2011 as Bar Chart.
#Is Bar Chart Better to visualize than Simple Plot?


# In[21]:


plt.bar(sales_2011_month.index,sales_2011_month.values,color="red") # Change the color and play
plt.xlabel("Sales in Euro")
plt.ylabel("Month Number")
plt.title("Sales Per Month in Year 2011")
plt.show()


# In[22]:


#3. Plot Pie Chart for Year 2011 Country Wise. 
#Which Country contributes highest towards sales?


# In[23]:


sales_country_wise = sales_2011.groupby('Country').sum()['Amount']

plt.title("Country Wise Contribution For 2011")

plt.pie(sales_country_wise.values,labels=sales_country_wise.index,autopct='%1.1f%%')

plt.show()


# In[24]:


#4. Plot Scatter Plot for the invoice amounts and see the concentration of amount.
#In which range most of the invoice amounts are concentrated.


# In[25]:


#Get Invoice Number and Sum of Sales
sales_invoice_wise = sales_2011.groupby('InvoiceNo').sum()['Amount']
print(sales_invoice_wise)


# In[26]:


#Create Scatter Plot
plt.scatter(sales_invoice_wise.values,sales_invoice_wise.values)
plt.grid(True)
plt.show()


# In[ ]:


#Completed.

