#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Find k largest element using heaps
import heapq
def kLargestElement(nums,k):
    heap=nums[:k]
    heapq.heapify(heap)
    for i in range(k,len(nums)):
        if nums[i]>heap[0]:
            heapq.heapreplace(heap,nums[i])
    return heap[0]

nums=[3,2,3,1,2,4,5,5,6]
k=4
kLargestElement(nums,k)


# In[22]:


# Find k smallest element using heaps
import sys
def kLargestElement(nums,k):
    heap=nums[:k]
    heapq.heapify(heap)
    count=0
    for i in range(k,len(nums)):
        heapq.heapreplace(heap, nums[i])
        count+=1
        if count==k-1:
            return heap[0]
    if count<k:
        for i in range(count,k):
            heapq.heapreplace(heap, sys.maxint)
            count+=1
            if count==k-1:
                return heap[0]
    
    
nums=[3,2,3,1,2,4,5,5,6]
k=8
kLargestElement(nums,k)


# In[49]:


# Largest kth element using quick sort
def klargestelement(nums, k):
    if k>0 and k <= len(nums):
        pos=partition(nums,0,len(nums)-1)
        if pos<len(nums)-k:
            return klargestelement(nums[pos+1:],k)
        elif pos>len(nums)-k:
            return klargestelement(nums[:pos],k-(len(nums)-pos))
        else:
            return nums[pos]
        
def partition(nums, l, r):
    x=nums[r]
    j=0
    for i in range(l, r):
        if nums[i]<x:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
            
    nums[r],nums[j]=nums[j],nums[r]
    return j
            
nums=[3,2,3,1,2,4,5,5,6]
klargestelement(nums,2)

