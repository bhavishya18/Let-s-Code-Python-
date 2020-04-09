#!/usr/bin/env python
# coding: utf-8

# In[92]:


# 

class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
class CodeDecode:
    def serialize(self, root):
        if not root:
            return "#"
        s = "{},{},{}".format(root.val, self.serialize(root.left), self.serialize(root.right))
        return s
        
    
    def deserialize(self,data):
        d = iter(data.split(','))
        
        def helper(d):
            root = next(d)
            if root == "#":
                return None
            root = TreeNode(root)
            root.left = helper(d)
            root.right = helper(d)
            return root
        return helper(d)
                    
t=TreeNode(1)
t.left=TreeNode(2)
t.left.right=TreeNode(5)
t.right=TreeNode(3)
t.right.right=TreeNode(7)
cd=CodeDecode()
cd.deserialize(cd.serialize(t))


# In[ ]:


# Serialization using BFS
    def serialize(root):
        node=[]
        result=[]
        node.append(root)
        result.append(root.val)
        while node:
            parents=node
            node=[]
            for i in parents:
                if i.left:
                    node.append(i.left)
                    result.append(i.left.val)
                else:
                    result.append("#")
                if i.right:
                    node.append(i.right)
                    result.append(i.right.val)
                else:
                    result.append("#")
        r=""
        for i in result:
            r+=str(i)
            r+=","
        return r

