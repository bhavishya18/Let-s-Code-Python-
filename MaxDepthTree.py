#!/usr/bin/env python
# coding: utf-8

# In[2]:


class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def TreeMaxDepth(root):
    node=[]
    node.append(root)
    count=0
    while node:
        count+=1
        parents=node
        node=[]
        for i in parents:
            if i.left!=None:
                node.append(i.left)
                
            if i.right!=None:
                node.append(i.right)
                
    return count

    
    
t = TreeNode(3)
t.left=TreeNode(9)
t.right=TreeNode(20)
# t.left.left=TreeNode(3)
# t.left.right=TreeNode(3)
t.right.right=TreeNode(7)
t.right.left=TreeNode(15)
TreeMaxDepth(t)


# In[16]:


def TreeMDepth(root):
    if root==None:
        return
    
    if root.left==None and root.right==None:
        return 1
    if root.left==None:
        
        return TreeMDepth(root.right)+1
    if root.right==None:
        return TreeMDepth(root.left)+1
                
    return max(TreeMDepth(root.left),TreeMDepth(root.right))+1

t = TreeNode(3)
t.left=TreeNode(9)
t.right=TreeNode(20)
t.left.left=TreeNode(3)
t.left.right=TreeNode(3)
t.right.right=TreeNode(7)
t.right.left=TreeNode(15)
t.right.left.left=TreeNode(15)
t.right.left.left.left=TreeNode(15)

TreeMDepth(t)

