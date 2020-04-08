#!/usr/bin/env python
# coding: utf-8

# In[8]:


import collections
def validAnagram(s, t):
    if len(s)!=len(t):
        return False
    anagram=collections.defaultdict(int)
    for i in s:
        anagram[i]+=1
    for i in t:
        if i not in anagram:
            return False
        elif anagram[i]==0:
            return False
        else:
            anagram[i]-=1
    return True


s="anagram"
t="nagaram"
u="rat"
v="car"
validAnagram(u,v)


# In[12]:


def validAnag(s, t):
    if len(s)!=len(t):
        return False
    anagram=[0]*26
    for i in s:
        anagram[ord(i)-ord('a')]+=1
    print anagram
    for i in t:
        if anagram[ord(i)-ord('a')]==0:
            return False
        else:
            anagram[ord(i)-ord('a')]-=1
    return True
s="anagram"
t="nagaram"
u="rat"
v="car"
validAnag(s,t)


# In[ ]:




