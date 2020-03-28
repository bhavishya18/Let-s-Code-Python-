#!/usr/bin/env python
# coding: utf-8

# In[33]:


def atoi(str):
    str=str.strip()
    if str == None or str=="":
        return 0
    if str[0]=="-":
        sign = -1
        str = str[1:]
    elif str[0] == "+":
        sign = 1
        str = str[1:]
    else:
        sign =1
    if str == "" or str==None:
        return 0
    num = 0
    for i in str:
        if i.isdigit():
            i = int(i)
            num=num*10+i
        else:
            break
    num = int(num) * sign
    return min(2**31-1, max(num, -2**31))
    
s = str(input("Enter a string:"))
atoi(s)


# In[ ]:





# In[ ]:




