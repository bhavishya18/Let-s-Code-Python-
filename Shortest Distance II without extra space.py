#!/usr/bin/env python
# coding: utf-8

# In[6]:


#  Shortest distance II withour using extra space

import sys
from collections import defaultdict
class Distance:
    def __init__(self, lst):
        self.locations=lst
    def ShortestDistance(self, word1, word2):
        mindist=len(self.locations)
        for i in range(0,len(self.locations)):
            if self.locations[i]==word1 or self.locations[i]==word2:
                prev=i
                break
        while i<len(self.locations):
            if self.locations[i]==word1 or self.locations[i]==word2:
                if self.locations[i]!=self.locations[prev] and i-prev<mindist:
                    mindist=i-prev
                    prev=i
                else:
                    prev=i
            i+=1
        return mindist


            
words=["Developer","codes","makes","practice", "Developer","codes","apple","makes"]
loc=Distance(words)
loc.ShortestDistance("Developer","codes")


# In[ ]:




