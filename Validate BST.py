#!/usr/bin/env python
# coding: utf-8

# In[9]:


class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def ValidateBST(root, min, max):
    if root==None:
        return True
    if (min!=None and root.val<=min) or (max!=None and root.val>=max):
        return False
    if not ValidateBST(root.left, min, root.val) or not ValidateBST(root.right, root.val, max):
        return False
    return True
    
    
t = TreeNode(5)
t.left=TreeNode(1)
t.right=TreeNode(4)
t.left.left=TreeNode(None)
t.left.right=TreeNode(None)
t.right.right=TreeNode(6)
t.right.left=TreeNode(3)
ValidateBST(t, None, None)

