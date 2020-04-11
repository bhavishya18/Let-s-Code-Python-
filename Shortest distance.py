#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Shortest distance between 2 words

def ShortestDistance(lst, word1, word2):
    mindist=len(lst)
    for i in range(0,len(lst)):
        if lst[i]==word1 or lst[i]==word2:
            prev=i
            break
    while i<len(lst):
        if lst[i]==word1 or lst[i]==word2:
            if lst[i]!=lst[prev] and i-prev<mindist:
                mindist=i-prev
                prev=i
            else:
                prev=i
        i+=1
    return mindist-1

l=["practice","is","perfect", "practice", "coder"]
ShortestDistance(l,"practice","coder")


# In[ ]:




