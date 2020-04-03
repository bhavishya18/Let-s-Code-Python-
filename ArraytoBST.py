#!/usr/bin/env python
# coding: utf-8

# In[28]:


import math
from collections import deque
class TreeNode:
    def __init__(self,t):
        self.val=t
        self.left=None
        self.right=None


def atoBST(array):
    n=len(array)
    if n==0:
        return
    mid=int(math.floor(n/2))
    
    root=TreeNode(array[mid])
    root.left=atoBST(array[0:mid])
    root.right=atoBST(array[mid+1:n])
    return root


    
num = [-10,-3,0,5,9]
t=atoBST(num)

def printt(node):
    q=deque()
    q.append(node)
    while q:
        p=q.popleft()
        print p.val
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)
    return 

printt(t)


# In[ ]:




