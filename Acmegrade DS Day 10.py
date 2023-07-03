#!/usr/bin/env python
# coding: utf-8

# In[30]:


#Day 10


# In[31]:


#Read the three csv files which contains the score of same students in term1 for each Subject.


# In[32]:


import pandas as pd
import numpy as np
math_data = pd.read_csv("D:\Study Material\Data Science\Acmegrade\Day 10\CS 16 Ans -Data Transformation-2\MathScoreTerm1.csv")
math_data.head()


# In[33]:


ds_data = pd.read_csv("D:\Study Material\Data Science\Acmegrade\Day 10\CS 16 Ans -Data Transformation-2\MathScoreTerm1.csv")
ds_data.head()


# In[34]:


physics_data = pd.read_csv("D:\Study Material\Data Science\Acmegrade\Day 10\CS 16 Ans -Data Transformation-2\PhysicsScoreTerm1.csv")
physics_data.head()


# In[35]:


math_data = math_data.drop(['Name','Ethinicity'], axis=1)
print(math_data.head())


# In[36]:


print(ds_data.columns)


# In[37]:


ds_data = ds_data.drop(['Name', 'Ethinicity'],axis=1)
print(ds_data.head())


# In[38]:


print(physics_data.columns)


# In[41]:


physics_data=physics_data.drop(['Name','Ethinicity'],axis=1)
print(physics_data.head())


# In[42]:


#Fill missing score data with zero.


# In[43]:


print (math_data.isnull().sum())


# In[44]:


math_data['Score'] = math_data['Score'].fillna(0)
print (math_data.isnull().sum())


# In[45]:


print (ds_data.isnull().sum())


# In[47]:


ds_data['Score'] = ds_data['Score'].fillna(0)
print (ds_data.isnull().sum())


# In[48]:


print (physics_data.isnull().sum())


# In[49]:


physics_data['Score'] = physics_data['Score'].fillna(0)
print (physics_data.isnull().sum())


# In[50]:


#Merge the three files.


# In[51]:


all_data =[math_data,ds_data,physics_data]
all_data


# In[52]:


for dataset in all_data:
    dataset['Sex'] = dataset['Sex'].map({'M': 1, 'F': 2}).astype(int)


all_data_df = pd.concat(all_data)
all_data_df


# In[53]:


all_data_df.to_csv("D:\Study Material\Data Science\Acmegrade\Day 10\CS 16 Ans -Data Transformation-2\ScoreFinal.csv",index=False)

print ("Done")


# In[ ]:




