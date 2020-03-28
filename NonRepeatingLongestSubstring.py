#!/usr/bin/env python
# coding: utf-8

# In[35]:


def LongestSubstring(str):
    maxval = 0
    hset = set()
    i = j = 0
    n = len(str)
    while i<n and j<n:
        #insertion in set
        if str[i] not in hset:
            hset.add(str[i])
            i += 1
            maxval = max(maxval, i- j)
        else:
            hset.remove(str[j])
            j +=1
    return [maxval, str[j:i]]

                
string1 = input("Enter String")
LongestSubstring(string1)


# In[ ]:




