#!/usr/bin/env python
# coding: utf-8

# In[12]:


import sys
from collections import defaultdict
class Distance:
    def __init__(self, lst):
        self.locations=defaultdict(list)
        n=len(lst)
        for i in range(n):
            self.locations[lst[i]].append(i)
    def ShortestDistance(self, word1, word2):
        word1_loc = self.locations[word1]
        print word1_loc
        word2_loc = self.locations[word2]
        print word2_loc
        i=0
        j=0
        min_distance=sys.maxint
        while i<len(word1_loc) and j<len(word2_loc):
            temp=abs(word1_loc[i]-word2_loc[j])
            print temp
            min_distance=min(min_distance,temp)
            print min_distance
            if i>j:
                i+=1
            else:
                j+=1
        return min_distance
            
words=["Developer","codes","makes","practice", "Developer","Bhavishya","apple","makes"]
loc=Distance(words)
loc.ShortestDistance("Developer","makes")

