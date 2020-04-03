#!/usr/bin/env python
# coding: utf-8

# In[6]:


class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
def PathSum(root, sumval):
    if root==None:
        return False
    sumval=sumval-root.val
    if root.left ==None and root.right==None and sumval==0:
        return True
    return PathSum(root.left, sumval) or PathSum(root.right, sumval)

t = TreeNode(5)
t.left = TreeNode(1)
t.left.left = TreeNode(11)
t.left.left.left = TreeNode(7)
t.left.left.right = TreeNode(2)
t.right = TreeNode(8)
t.right.left = TreeNode(13)
t.right.right = TreeNode(4)
t.right.right.right = TreeNode(5)
PathSum(t, 22)


# In[ ]:




