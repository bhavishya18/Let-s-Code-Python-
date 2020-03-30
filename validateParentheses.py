#!/usr/bin/env python
# coding: utf-8

# In[4]:


def validPar(str):
    if str == None or str=="":
        return False
    stack = []
    for i in str:
        if i == '(' or i=='{' or i=='[':
            stack.append(i)
        elif i == ')':
            el = stack.pop()
            if el == '(':
                continue
            else:
                return False
        elif i == ']':
            el = stack.pop()
            if el == '[':
                continue
            else:
                return False
        elif i == '}':
            el = stack.pop()
            if el == '{':
                continue
            else:
                return False
    return True


# In[16]:


str = input("Enter a string: ")
validPar(str)


# In[ ]:




