#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Solution(object):
    def dfs(self,grid,i,j,row_len,col_len):
        if i >=row_len or j>=col_len or i<0 or j<0:
            return 
        if grid[i][j]=="0" or grid[i][j] == "2":
            return 
        else:
            grid[i][j]="2"
            self.dfs(grid,i+1,j,row_len,col_len)
            self.dfs(grid,i,j+1,row_len,col_len)
            self.dfs(grid,i,j-1,row_len,col_len)
            self.dfs(grid,i-1,j,row_len,col_len)
    def numIslands(self, grid):
        
        row_len=len(grid)
        if row_len == 0:
            return 0
        col_len=len(grid[0])
        count=0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j,row_len,col_len)
                    count+=1       
                    
        return count
    
    


# In[ ]:




