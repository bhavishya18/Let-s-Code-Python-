#!/usr/bin/env python
# coding: utf-8

# In[7]:


class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def TreeTraversal(root):
    node=[]
    result=[]
    valuenode=[root.val]
    node.append(root)
    while node:
        result.append(valuenode)
        valuenode=[]
        parents=node
        node=[]
        for i in parents:
            if i.left!=None:
                node.append(i.left)
                valuenode.append(i.left.val)
            if i.right!=None:
                node.append(i.right)
                valuenode.append(i.right.val)
    return result

    
    
t = TreeNode(3)
t.left=TreeNode(9)
t.right=TreeNode(20)
# t.left.left=TreeNode(3)
# t.left.right=TreeNode(3)
t.right.right=TreeNode(7)
t.right.left=TreeNode(15)
TreeTraversal(t)


# In[ ]:




