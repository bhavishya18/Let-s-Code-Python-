#!/usr/bin/env python
# coding: utf-8

# In[4]:


def ReverseWords(string):
    s=string.split(" ")
    result=[]
    for i in s:
        result.insert(0,i)
    return " ".join(result)


