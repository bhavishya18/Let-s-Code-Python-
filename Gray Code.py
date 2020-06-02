#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Solution(object):
    def grayCode(self, n):
        result=[0]
        for i in range(n):
            result+=[num+2**i for num in reversed(result)]
        return result
    
s=Solution()
s.grayCode(4)


# In[ ]:




