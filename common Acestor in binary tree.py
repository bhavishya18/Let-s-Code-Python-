#!/usr/bin/env python
# coding: utf-8

# In[10]:


class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def commonAnc(root, p, q):
    stack=[root]
    parent = {root:None}
    while p not in parent or q not in parent:
        s=stack.pop()
        print s.val
        if s.left:
            stack.append(s.left)
            parent[s.left]=s
        if s.right:
            stack.append(s.right)
            parent[s.right]=s
    ancestor=set()    
    print parent
    while p:
        ancestor.add(p)
        p=parent[p]
    while q not in ancestor:
        q=parent[q]
    print q.val
    return q

t=TreeNode(3)
t.left=TreeNode(5)
t.right=TreeNode(1)
t.left.left=TreeNode(6)
t.left.right=TreeNode(2)
t.left.right.left=TreeNode(7)
t.left.right.right=TreeNode(4)
t.right.left=TreeNode(0)
t.right.right=TreeNode(8)

commonAnc(t, t.left, t.left.right.right)


# In[ ]:




