#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
def ShortestDistance3(words, word1, word2):
    if word1==word2:
        for i in range(len(words)):
            if words[i]==word1:
                prev=i
                break
        min_dist=sys.maxint
        while i<len(words):
            if words[i]==words[prev] and i!=prev:
                min_dist=min(min_dist,i-prev)
                prev=i
            i+=1
    else:
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                prev=i
            break
        min_dist=sys.maxint
        while i <len(words):
            if words[i]!=words[prev]:
                min_dist=min(min_dist,i-prev)
                prev=i
            else:
                prev=i
            i+=1
    return min_dist
words=["Developer","codes","makes","practice", "Developer","codes","apple","makes"]

print ShortestDistance3(words,"Developer","codes")
print ShortestDistance3(words,"codes","codes")


# In[ ]:




