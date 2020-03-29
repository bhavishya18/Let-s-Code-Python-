#!/usr/bin/env python
# coding: utf-8

# In[19]:


def phone_num(num):
    phone = {"2":['a','b','c'], "3":['d','e','f'], "4":['g','h','i'],
        "5":['j','k','l'], "6":['m','n','o'], "7":['p','q','r','s'],
        "8":['t','u','v'], "9":['w','x','y','z']}
    q=[]
    q.append("")
    n=len(num)
    result=[]
    while q:
        element=q.pop()
        if len(element)==n:
            result.append(element)
        else:
            for i in phone[num[len(element)]]:
                q.append(element+i)
    return result

num = str(input("Enter a number: "))
phone_num(num)


# In[ ]:




