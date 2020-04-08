#!/usr/bin/env python
# coding: utf-8

# In[30]:


class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def TreePaths(root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        return root
    else:
        result=[]
        node=[]
        allpaths=SeparateNode(root, node, result)
        for i in range(len(allpaths)):
            allpaths[i]="->".join(allpaths[i])
        return allpaths
    
def SeparateNode(root, node, result):
    
    if root==None:
        return
    if root.left==None and root.right==None:
        node=node+[str(root.val)]
        result.append(node)
        return
    node =node+[str(root.val)]
    SeparateNode(root.left, node, result) 
    SeparateNode(root.right, node, result)
        
    return result


t=TreeNode(1)
t.left=TreeNode(2)
t.left.right=TreeNode(5)
t.right=TreeNode(3)
TreePaths(t)


# In[ ]:




