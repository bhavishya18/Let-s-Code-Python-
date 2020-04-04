#!/usr/bin/env python
# coding: utf-8

# In[14]:


import sys
def BuySellStock(nums):
    if nums==None or nums==[]:
        return 0
    sum = 0
    buy=sys.maxint
    for i in range(0,len(nums)):
        if nums[i]<buy:
            buy=nums[i]
        elif nums[i]-buy>sum:
            sum=nums[i]-buy
        
    return sum

nums = [2,4,1]
testcase2 = [2,1,2,1,0,1,2]
BuySellStock(nums)


# In[15]:


BuySellStock(testcase2)


# In[ ]:




