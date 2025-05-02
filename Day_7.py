#!/usr/bin/env python
# coding: utf-8

# ## Strings Slicing and Operations on Strings in Python
# ### Length of a String: 
# We can find the length of a string using len() function.

# In[2]:


Name = "Samarth"
print(len(Name))


# In[3]:


Name = "Mango"
len1 = len(Name)
print("Mango is a", len1,"letter word")


# ### String as an array
# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

# In[19]:


Fruit = "Apple"
print(Fruit[:2]) 
print(Fruit[0:3])
print(Fruit[4])#returns character at specified index


# This method of specifying the start and end index to specify a part of a string is called slicing.
# ### Slicing Example:

# In[20]:


pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index


# In[26]:


Fruit = "Apple"
print(Fruit[:4])
print(Fruit[4:])
print(Fruit[1:3])
print(Fruit[-4:])
print(Fruit[len(Fruit)-4:])


# In[27]:


alphabets = "ABCDE"
for i in alphabets:
    print(i)


# In[30]:


nm = "Harry"
print(nm[-4:2])
print(nm[len(nm)-4:2])


# In[ ]:




