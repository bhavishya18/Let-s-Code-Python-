#!/usr/bin/env python
# coding: utf-8

# In[38]:


def sumofthreenums(nums):
    nums.sort()
    print nums
    result = []
    for i in range(0,len(nums)-2):
        if i!=0 and nums[i]==nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left<right:
            if nums[i]+nums[left]+nums[right]==0 :
                list=[nums[i],nums[left],nums[right]]
                if list not in result:
                    result.append(list)
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1
            elif nums[i]+nums[left]+nums[right] < 0:
                left+=1
            else:
                right-=1
    return result

nums = input("Enter a array of numbers: ")
sumofthreenums(nums)


# In[ ]:


-2, -1, -1, 0, 2, 3
-2, -1, 3

