#!/usr/bin/env python
# coding: utf-8

# In[6]:


def longestpalsubstring(str):
    n=len(str)
    if n==1:
        return str
    if n==2 and str[0]==str[1]:
        return str
    low=0
    high = 0
    maxlength=1
    for i in range(1, n):
        low = i-1
        high = i
        while low >=0 and high <n and str[low]==str[high]:
            if high-low+1 > maxlength:
                start=low
                maxlength = high-low+1
            low-=1
            high+=1
        low= i-1
        high = i +1
        while low >=0 and high <n and str[low]==str[high]:
            if high-low+1 > maxlength:
                start=low
                maxlength = high-low+1
            low-=1
            high+=1
    return str[start:start+maxlength]

str=input("Enter string:")
longestpalsubstring(str)

