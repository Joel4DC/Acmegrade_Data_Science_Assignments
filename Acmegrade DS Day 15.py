#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day 15


# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


#Load Data Set 

prisoners = pd.read_csv("D:\Professional\Data Science\Acmegrade\Day 15\CS 24 Ans -Data Pre-processing-1\prisoners.csv")
prisoners.head()


# In[20]:


#1.Load the dataset “prisoners.csv” using pandas and display the first and last five rows in the dataset.


# In[21]:


prisoners.tail()


# In[22]:


prisoners.head()


# In[23]:


#2. Use describe method in pandas and find out the number of columns. 
#Can you say something about those rows who have zero inmates?


# In[24]:


prisoners.describe()
zero_indexes = prisoners.loc[prisoners['No. of Inmates benefitted by Elementary Education']==0]
zero_indexes


# In[25]:


#3. Create a new column -’total_benefitted’ that is a sum of inmates benefitted through all modes.


# In[26]:


prisoners["total_benefited"]=prisoners.iloc[:,2:].sum(axis=1)
prisoners


# In[27]:


#4. Create a new row - “totals” that is the sum of all inmates benefitted through each mode across all states.


# In[28]:


prisoners_total = prisoners.append(prisoners.iloc[:, 2:].sum(numeric_only=True), ignore_index=True)

prisoners_total


# In[29]:


#Plotting:

#5. Make a bar plot with each state name on the x -axis and their total benefitted inmates as their bar heights.
#Which state has the maximum number of beneficiaries?


# In[30]:


xlabels = prisoners['STATE/UT'].values

plot.figure(figsize=(20, 10))
plot.xticks(np.arange(xlabels.shape[0]),xlabels,rotation='vertical', fontsize=18)
plot.xticks

plot.bar(np.arange(prisoners.values.shape[0]),prisoners['total_benefited'],align='edge')


# In[31]:


#6. Make a pie chart that depicts the ratio among different modes of benefits.


# In[32]:


labels = prisoners.columns[2:-1]
sizes = prisoners_total.iloc[-1][2:-1].values
fig1, ax1 = plot.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plot.show()


# In[33]:


#Completed.


# In[ ]:




