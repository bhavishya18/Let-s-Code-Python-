#!/usr/bin/env python
# coding: utf-8

# In[7]:


def rotatematrix(matrix):
    if matrix==None:
        return
    result = []
    submat= []
    n=len(matrix)
    for i in range(0, n):
        submat= []
        for j in range(n-1,-1,-1):
            submat.append(matrix[j][i])
        result.append(submat)
         
    return result
  

matrix  = [
    [1,2,3],
  [4,5,6],
  [7,8,9]
]

matrix2  = [
  [1,2],
  [4,6]
]

print rotatematrix(matrix)
print rotatematrix(matrix2)


# In[ ]:




