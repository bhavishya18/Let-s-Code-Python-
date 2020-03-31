#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import defaultdict

def groupAnagram(str):
    anagram = defaultdict(list)
    for i in str:
        anagram[tuple(sorted(i))].append(i)
    return anagram.values()

def groupAnagram2(str):
    anagram = defaultdict(list)
    for i in str:
        l = [0] * 26
        for j in i:
            l[ord(j)-ord('a')]+=1
        anagram[tuple(l)].append(i)
    return anagram.values()


le = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagram2(le)


# In[ ]:




