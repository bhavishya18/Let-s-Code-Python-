#!/usr/bin/env python
# coding: utf-8

# In[4]:


class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def lowestcommonancestor(root, p, q):
    if p>root.val and q>root.val:
        return lowestcommonancestor(root.right, p, q)
    elif p<root.val and q<root.val:
        return lowestcommonancestor(root.left, p, q)
    else:
        return root.val
    
t=TreeNode(6)
t.left=TreeNode(2)
t.right=TreeNode(8)
t.left.left=TreeNode(0)
t.left.right=TreeNode(4)
t.left.right.left=TreeNode(3)
t.left.right.right=TreeNode(5)
lowestcommonancestor(t, 3, 4)


# In[ ]:




