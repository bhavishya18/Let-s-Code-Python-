#!/usr/bin/env python
# coding: utf-8

# In[1]:


def subset(nums):
    output=[]
    n=len(nums)
    for i in range(2**n,2**(n+1)):
        bitmask = bin(i)[3:]
        output.append([nums[j] for j in range(n) if bitmask[j]=='1'])
    return output

nums = [1,2,3]
r= subset(nums)
print r


# Other way of doing this

def Subset(nums):
    result = [[]]
    for i in nums:
        result+=[j+[i] for j in result]
    return result

nums = nums = [5,9,0]
r= Subset(nums)
print r


# In[ ]:




