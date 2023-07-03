#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Acmegrade DS Day 4


# In[2]:


#1. Write a Python program to sum all the items in a list.


# In[3]:


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


print(sum_list([1,2,-8]))


# In[4]:


#2. Write a Python program to multiplies all the items in a list


# In[7]:


def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot



print(multiply_list([1,2,-8]))


# In[ ]:


#3. Write a Python program to get the largest number from a list. 


# In[6]:


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max



print(max_num_in_list([1, 2, -8, 0]))


# In[8]:


#4. Write a Python program to get the smallest number from a list.


# In[9]:


def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))


# In[10]:


#5. Write a Python program to count the number of strings where the string length is 2 
#or more and the first and last character are same from a given list of strings.


# In[11]:


def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


# In[12]:


#6. Write a Python program to get a list, sorted in 
#increasing order by the last element in each tuple from a given list of non-empty tuples.  


# In[13]:


#i


# In[23]:


x = [2, 8, 1, 4, 6, 3, 7]

print("Sorted List returned:")
print(sorted(x))


# In[25]:


print("\nReverse sort:")
print(sorted(x, reverse=True))


# In[26]:


x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6}
print (sorted(x))


# In[27]:


x = {'q', 'w', 'e', 'r', 't', 'y'}
print (sorted(x))


# In[28]:


x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print (sorted(x))


# In[29]:


#ii


# In[30]:


L = ["cccc", "b", "dd", "aaa"]
print ("Normal sort :", sorted(L))
print ("Sort with len :", sorted(L, key = len))


# In[31]:


#iii


# In[32]:


def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[34]:


#7. Write a Python program to remove duplicates from a list.


# In[35]:


a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)


# In[36]:


#8. Write a Python program to check a list is empty or not.


# In[37]:


l = []
if not l:
  print("List is empty")


# In[40]:


#9. Write a Python program to clone or copy a list.


# In[41]:


#i


# In[42]:


original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)


# In[43]:


#ii


# In[44]:


original_list = [10, 22, 44, 23, 4]
new_list = original_list.copy()
print(original_list)
print(new_list)


# In[45]:


#10. Write a Python program to find the list of words that are longer than n from a given list of words.


# In[46]:


def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	

print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# In[47]:


#11. Write a Python function that takes two lists and returns True if they have at least one common member.


# In[48]:


def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result


print(common_data([1,2,3,4,5], [5,6,7,8,9]))

print(common_data([1,2,3,4,5], [6,7,8,9]))


# In[51]:


#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 


# In[52]:


#i


# In[53]:


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


# In[54]:


#ii


# In[56]:


l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print(obj1)
print(obj2)

print(list(enumerate(l1)))
print(list(enumerate(s1)))


# In[57]:


# changing start index to 2 from 0
print (list(enumerate(s1,2)))


# In[ ]:


#Completed

