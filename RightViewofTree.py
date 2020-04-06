#!/usr/bin/env python
# coding: utf-8

# In[20]:


from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None
def RightView(root):
    right_View=dict()
    depth=-1
    q=deque([(root,0)])
    while q:
        
        node, d = q.popleft()
        
        if node is not None:
            maxdepth=max(depth,d)
            right_View[d]=node.val
            q.append((node.left,d+1))
            q.append((node.right,d+1))
    return [right_View[i] for i in range(maxdepth+1)]

t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
t.left.right=TreeNode(5)
t.right.right=TreeNode(4)
RightView(t)


# In[ ]:




