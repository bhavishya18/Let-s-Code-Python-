#!/usr/bin/env python
# coding: utf-8

# In[13]:


def countPrimes(num):
    if num<=2:
        return 0
    if num==3:
        return 1
    Flag=['True']*num
    Flag[0]='False'
    Flag[1]='False'
    count=0
    for i in range(2,num):
        if Flag[i]=='False':
            continue
        for j in range(i*i,num,+i):
            Flag[j]='False'
    for i in range(2,num):
        if Flag[i]=='True':
            count+=1
    return count



# In[ ]:




