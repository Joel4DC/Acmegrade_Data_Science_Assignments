#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Day 14


# In[2]:


#Business challenge/requirement
#SFO Public Department - referred to as SFO has captured all the salary data of its employees from year 2011-2014.
#Now we are in year 2015 and the organization is facing some financial crisis.
#As first step HR wants to rationalize employee cost to save payroll budget.
#You have to do data manipulation and analysis on the salary data to answer specific questions for cost savings.

#Key issues
#Cost can be saved by figuring out the key pockets of high salaries

#Data volume
#Approx 150K records across files


#Business benefits
#Save at least 10% of employee cost by identifying and letting them go

#Approach to Solve
#You have to use the fundamentals of Pandas and answer the following 5 Questions.


# In[3]:


#1.Compute how much total salary cost has increased from year 2011 to 2014.


# In[4]:


#Import Libraries 

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[7]:


#Load Data set 
salary = pd.read_csv(r"D:\Study Material\Data Science\Acmegrade\Day 14\CS 22 Ans -Data Maniputations-2\Salaries.csv")
display (salary)


# In[8]:


#Data Checks  

display(salary.head())
print (salary.info())

display(salary.describe())


# In[9]:


#Total Salary by year   

sum_year = salary.groupby('Year').sum()['TotalPayBenefits']
print ( sum_year)


# In[10]:


#Salary cost has increased from year 2011 to 2014

mean_year = salary.groupby('Year').mean()['TotalPayBenefits']
print ( mean_year)


# In[11]:


#2.Which Job Title in Year 2014 has highest mean salary?


# In[12]:


#Display average salary for all years 

mean_title_year = salary.groupby(['Year','JobTitle']).mean()['TotalPayBenefits']
print ( mean_title_year)


# In[14]:


#Filter the salary for 2014,find the average, and display the maximum mean value


df_g = salary.query('Year == 2014') #getting 2014
df_g = df_g.filter(['JobTitle', 'TotalPayBenefits'])
maxi=df_g.groupby('JobTitle').mean()
highest_Salary = maxi[maxi["TotalPayBenefits"]== maxi["TotalPayBenefits"].max()]
print(highest_Salary)


# In[15]:


#3. How much money could have been saved in Year 2014 by stopping OverTimePay?


# In[16]:


over_time_pay_year = salary.groupby('Year').sum()['OvertimePay']
print ( over_time_pay_year)


# In[17]:


#4. Which are the top 5 common job in Year 2014 and how much do they cost SFO?


# In[18]:


top_job_title = salary[salary['Year'] == 2014]['JobTitle'].value_counts().head(5)
print (top_job_title)


# In[19]:


#Calculate Cost 

sum_cost = 0
for index,value in top_job_title.iteritems():
    print(index,value)
    sum_cost += sum(salary[ (salary['Year']== 2014) & (salary['JobTitle'] == index)]['TotalPayBenefits'])

print (" Total Cost of Top 5 Jobs in Year 2014 ", sum_cost)


# In[20]:


#5.Who was the top earning employee across all the years?


# In[21]:


top_sal = salary.groupby('EmployeeName').sum()['TotalPayBenefits']
print((top_sal.sort_values(axis=0,ascending = False)))


# In[ ]:


#Completed.

