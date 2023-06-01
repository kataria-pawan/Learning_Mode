#!/usr/bin/env python
# coding: utf-8

# ### Basics of Python
# 
# Fill valid code/values in place of blanks. 

# In[1]:


# Demo
# initialize variable 'msg' with the string 'Hello World'
msg = "Hello World"
print(msg)

# Solution
msg = "Hello World"


# In[2]:


# initialize variables 'a' and 'b' with 5 and 6 respectively
a = 5
b = 6

# add 'a' and 'b' and assign the result into a new variable 'c'
c = a + b
print(c)


# In[3]:


# build a function to add 2 numbers
def addition(x,y):
    return(x+y)

# use the function 'addition' to add 'a' and 'b'
addition(a,b)


# In[1]:


# create a list consisting of first 5 even numbers and print the list
my_list = [1,2,3,4,5]
print(my_list)


# In[2]:


# access the 3rd element of the list 'my_list'
my_list[2]


# In[3]:


# given below is a dictionary having 4 unique keys, i.e., 'name', 'age', 'gender', 'is_employed'
my_dict = {'name':'Smith',
           'age':34,
           'gender': 'Male',
           'is_employed': False}

# print 'my_dict'
print(my_dict)


# In[4]:


# access value under 'name' key from 'my_dict'
my_dict["name"]


# In[5]:


# update 'is_employed' key to True
my_dict.update({'is_employed': True})

# print the updated dictionary
print(my_dict)


# In[7]:


# use a for loop to print only even numbers from the first 20 numbers, i.e. 1-20
for i in range(1,21):
    if i % 2 == 0:
        print(i)


# ### Please download the file "data_python.csv".

# In[4]:


# import required libraries
import pandas as pd
import numpy as np


# In[5]:


## read data_python.csv using pandas
mydata = pd.read_csv("C:/Users/Pawan Kataria/Downloads/Assignment2/data_python.csv")


# In[6]:


## print the number of rows and number of columns of mydata
mydata.shape


# In[7]:


## assign a variable 'target' with the 'Loan_Status' feature from mydata dataframe
target = mydata["Loan_Status"]
print(target)


# In[8]:


## print the datatype of ApplicantIncome feature
print(mydata['ApplicantIncome'].dtypes)


# In[9]:


## conditional statement - print 'Yes' if the 21st element of 'Education' feature is 'Graduate' else print 'No'
if(mydata['Education'][20] == 'Graduate'):
    print("Yes")
else:
    print("No")


# In[10]:


## print 31st to 35th rows of mydata
mydata.iloc[31:36]


# In[11]:


## print first 5 rows of 2nd and 3rd column only
mydata.iloc[:5,1:3]

