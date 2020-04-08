#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Solution using O(n) space

def productArray(nums):
    prodLow=[0]*len(nums)
    prodHigh=[0]*len(nums)
    prodLow[0]=1
    prodHigh[len(nums)-1]=1
    for i in range(1,len(nums)):
        prodLow[i]=prodLow[i-1]*nums[i-1]
    for i in range(len(nums)-2,-1,-1):
        prodHigh[i]=prodHigh[i+1]*nums[i+1]
    for i in range(0,len(nums)):
        prodLow[i]=prodLow[i]*prodHigh[i]
    return prodLow
    
nums=[1,2,3,4]
productArray(nums)


# In[7]:


#  Solution using O(1) space

def productArray2(nums):
    n=len(nums)
    prod=[0]*n
    prod[0]=1
    for i in range(1,n):
        prod[i]=prod[i-1]*nums[i-1]
    R=1
    for i in range(n-1,-1,-1):
        prod[i]*=R
        R*=nums[i]
    return prod
nums=[1,2,3,4]
productArray2(nums)


# In[ ]:






