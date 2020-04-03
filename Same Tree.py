#!/usr/bin/env python
# coding: utf-8

# In[8]:


class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def SameTree(t1, t2):
    if t1==None and t2==None:
        return True
    if t1==None or t2==None:
        return False
    if t1.val!=t2.val:
        return False
    if not SameTree(t1.left, t2.left) and not SameTree(t1.right, t2.right):
        return False
    
    
    
t1 = TreeNode(1)

t1.left=TreeNode(2)
# t1.right=TreeNode(3)
t2 = TreeNode(1)
# t2.left=TreeNode(2)
t2.right=TreeNode(3)
SameTree(t1,t2)


# In[ ]:




