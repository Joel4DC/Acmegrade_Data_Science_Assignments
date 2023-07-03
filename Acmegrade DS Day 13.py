#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Day 13


# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
plt.rcParams["figure.figsize"] = (20,10)


# In[4]:


df = pd.read_csv("D:\Study Material\Data Science\Acmegrade\Day 13\CS 21 Ans -Data Maniputations-1\HollywoodMovies.csv", delimiter=',')
df


# In[6]:


#Find Rating
selected_columns = df.loc[:, ["Movie", "AudienceScore", "Story"]]
highest_rated = ""
rating = 0

for i in range(0, 970):
    if selected_columns.loc[i]["Story"] in ("Quest","quest") and selected_columns.loc[i]["AudienceScore"] > rating:
        rating = selected_columns.loc[i]["AudienceScore"]
        highest_rated = selected_columns.loc[i]["Movie"]

print(highest_rated,'-', rating)


# In[7]:


#Fnd the genre in which there has been the greatest number of movie releases.

#Genre and number of movies in each Genre.


# In[8]:


genre = df.loc[:, ["Genre"]]

frequency = dict()
for i in range(0, 970):
    if genre.loc[i][0] in frequency:
        frequency[str(genre.loc[i][0])] += 1
    else:
        frequency[str(genre.loc[i][0])] = 1
print(frequency)


# In[9]:


#Sort the frequency dictionary based on Values 

frequency_sorted = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
print (frequency_sorted)


# In[10]:


#Print the sorted value based on index 

for i in frequency_sorted:
	print(i[0],'-' ,i[1])


# In[11]:


#Genre in which there has been the maximum number of movies released

print (frequency_sorted[0])


# In[12]:


#Print the names of the top five movies with the costliest budgets.

top5budget = df.sort_values(by='Budget', ascending=False)
top5budget[['Movie','Budget']].head()


# In[13]:


#Is there any correspondence between the critics’ evaluation of a movie and its acceptance by the public?
#Find out, by plotting the net profitability of a movie against the ratings it receives on Rotten Tomatoes.


# In[14]:


selected = df.loc[:, ["Profitability", "RottenTomatoes"]]

plt.scatter(selected["Profitability"], selected["RottenTomatoes"])
plt.xlim(0, 200)
plt.xlabel('Profitability')
plt.ylabel('Rating')
plt.show()


# In[16]:


#5.1 From the raw data below create a data frame.

#'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
#'age': [42, 52, 36, 24, 73],
#'preTestScore': [4, 24, 31, ".", "."],
#'postTestScore': ["25,000", "94,000", 57, 62, 70]


# In[17]:


raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
print(df)


# In[18]:


#5.2 Save the dataframe into a csv file as example.csv.


# In[20]:


raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df.to_csv('example.csv')


# In[21]:


#5.3 Read the example.csv and print the data frame.


# In[22]:


df = pd.read_csv('example.csv')
print(df)


# In[23]:


#5.4: Read the example.csv without column heading.


# In[24]:


import pandas as pd
df = pd.read_csv('example.csv', header=None)
print(df)


# In[25]:


#5.5: Read the example.csv and make the index columns as 'First Name’ and 'Last Name'.


# In[26]:


df = pd.read_csv('example.csv', index_col=['First Name', 'Last Name'], names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
print(df)


# In[27]:


#5.6 Print the data frame in a Boolean form as True or False.
#True for Null/ NaN values and false for non-null values.


# In[29]:


df = pd.read_csv('example.csv', na_values=['.'])
print(pd.isnull(df))


# In[30]:


#5.7 Read the dataframe by skipping first 3 rows and print the data frame.


# In[32]:


df = pd.read_csv('example.csv', skiprows=4)
print(df)


# In[33]:


#5.8 Load a csv file while interpreting "," in strings around numbers as thousands seperators.
#Check the raw data 'postTestScore' column has, as thousands separator.
#Comma should be ignored while reading the data.
#It is default behaviour, but you need to give argument to read_csv function which makes sure commas are ignored.


# In[34]:


df = pd.read_csv('example.csv',  thousands=',')
print(df)


# In[35]:


#6. Perform Operations on Files

#6.1: From the raw data below create a Pandas Series


# In[36]:


#Print all elements in lower case

s = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(s.str.lower())


# In[37]:


#Print all the elements in upper case

s = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(s.str.upper())


# In[38]:


#Print the length of all the elements.

s = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(s.str.len())


# In[39]:


#6.2 From the raw data below create a Pandas Series.
#'Atul', 'John ', ' jack ', 'Sam'


# In[40]:


#Print all elements after stripping spaces from the left and right

s = pd.Index([' Atul', 'John ', ' jack ', 'Sam'])
print(s.str.strip())


# In[41]:


#Print all the elements after removing spaces from the left only

s = pd.Index([' Atul', 'John ', ' jack ', 'Sam'])
print(s.str.lstrip())


# In[42]:


#Print all the elements after removing spaces from the right only

s = pd.Index([' Atul', 'John ', ' jack ', 'Sam'])
print(s.str.rstrip())


# In[43]:


#6.3 Create a series from the raw data below
#'India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'


# In[44]:


#split the individual strings wherever ‘_’ comes and create a list out of it.

s = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
print(s.str.split('_'))


# In[45]:


#Access the 1st Element individual element of a list

s = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
print(s.str.split('_').str.get(1))


# In[46]:


#Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements.

s = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
print(s.str.split('_', expand=True))


# In[47]:


#6.4 Create a series 

#'A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'


# In[48]:


s = pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
print (s)
print(s.str.replace('^.a|dog', 'XX-XX ', case=False))


# In[49]:


#6.5 Create a series and remove dollar from the numeric values '12', '-$10', '$10,000'.


# In[50]:


s = pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
print (s)
print(s.str.replace('^.a|dog', 'XX-XX ', case=False))


# In[51]:


#6.5 Create a series and remove dollar from the numeric values '12', '-$10', '$10,000'.


# In[52]:


d = pd.Series(['12', '-$10', '$10,000'])
print(d.str.replace('$', ''))


# In[54]:


#6.6 Create a series and reverse all lower-case words.
#'india 1998', 'big country', np.nan


# In[55]:


pattern = r'[a-z]+'
replacement = lambda m: m.group(0)[::-1]
s = pd.Series(['india 1998', 'big country', np.nan])
print (s)

s=s.str.replace(pattern, replacement)
print(s)


# In[57]:


#6.7: Create pandas series and print true if value is alphanumeric 
#in series or false if value is not alpha numeric in series.

#'1', '2', '1a', '2b', '2003c'


# In[58]:


pattern = r'[0-9][a-z]'
print(pd.Series(['1', '2', '1a', '2b', '2003c']).str.contains(pattern))


# In[59]:


#6.8: Create pandas series and print true if value is containing ‘A’

#'1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'


# In[60]:


pattern = r'[0-9][a-z]'
print(pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c']).str.contains('A', na=False))


# In[61]:


#6.9 Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values

#'a', 'a|b', np.nan, 'a|c'


# In[63]:


s = pd.Series(['a', 'a|b', np.nan, 'a|c'])
print(s.str.get_dummies(sep='|'))


# In[64]:


#6.10 Create pandas dataframe having keys and ltable and rtable as below-

#'key': ['One', 'Two'], 'ltable': [1, 2]
#'key': ['One', 'Two'], 'rtable': [4, 5]


# In[65]:


#Merge both the tables based of key

left = pd.DataFrame({'key': ['One', 'Two'], 'ltable': [1, 2]})
right = pd.DataFrame({'key': ['One', 'Two'], 'rtable': [4, 5]})
new=pd.merge(left, right, on='key')
print(new)


# In[ ]:


#Completed.

