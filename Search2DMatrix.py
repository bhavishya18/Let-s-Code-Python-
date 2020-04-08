#!/usr/bin/env python
# coding: utf-8

# In[4]:


def searchMatrix(matrix, target):
    if matrix==[] or matrix==[[]]:
        return False
    if target<matrix[0][0] or target>matrix[-1][-1]:
        return False
    row=len(matrix)
    col=len(matrix[0])
    i=0
    j=col-1
    while i>=0 and i<row and j>=0 and j<col:
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]>target:
            j-=1
        else:
            i+=1
    return False


matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
searchMatrix(matrix,17)


# In[ ]:




