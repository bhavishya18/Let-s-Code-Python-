#!/usr/bin/env python
# coding: utf-8

# In[4]:


def twoSum(nums, target):
    low=0
    high=len(nums)-1
    while low<high:
        if target-nums[low]==nums[high]:
            return [low+1,high+1]
        elif target-nums[low]<nums[high]:
            high-=1
        else:
            low+=1
            
            
numbers = [2,7,11,15]
twoSum(numbers,13)


# In[ ]:




