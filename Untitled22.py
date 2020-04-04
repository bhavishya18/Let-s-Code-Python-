#!/usr/bin/env python
# coding: utf-8

# In[5]:


def houseRobber(nums):
    if len(nums)==0:
        return 0
    if len(nums)==1:
        return nums[0]
    if len(nums)==2:
        return max(nums[0], nums[1])
    stack=[]
    stack.append(nums[0])
    stack.append(max(nums[0],nums[1]))
    for i in range(2,len(nums)):
        if stack[i-2]+nums[i]>stack[i-1]:
            stack.append(stack[i-2]+nums[i])
        else:
            stack.append(stack[i-1])
    return stack[-1]
    
nums=[2,1,1,2]
houseRobber(nums)


# In[ ]:




