#!/usr/bin/env python
# coding: utf-8

# In[1]:


name=input()
Dob=input()
Number=input()

password=Number[0:3]+name[-3:]+Dob[-4:]
print(password)

