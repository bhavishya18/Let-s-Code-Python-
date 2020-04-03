#!/usr/bin/env python
# coding: utf-8

# In[4]:


class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def SymmetricTree(root):
    if root==None:
        return True
    if root.left.val!=root.right.val:
        return False
    return findtree(root.left,root.right)
def findtree(t1, t2):
    if (t1.left==None and t2.right==None) or (t1.right==None and t2.left==None):
        return True
    if (t1.left==None or t2.right==None) or (t1.right==None or t2.left==None):
        return False
    if (t1.left.val!=t2.right.val) or (t1.right.val!=t2.left.val):
        return False
    return findtree(t1.left,t2.right) and findtree(t1.right,t2.left)
    
    
t = TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(2)
# t.left.left=TreeNode(3)
t.left.right=TreeNode(3)
t.right.right=TreeNode(3)
# t.right.left=TreeNode(4)
SymmetricTree(t)


# In[ ]:




