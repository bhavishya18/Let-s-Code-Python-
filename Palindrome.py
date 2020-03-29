#!/usr/bin/env python
# coding: utf-8

# In[7]:


def palindrome(num):
    if num<0:
        return False
    num=str(num)
    n=len(num)
    low=0
    high=n-1
    while low<high:

        if num[low]==num[high]:
            low+=1
            high-=1
        else:
            return False
    return True

num = input("Enter a number: ")
palindrome(num)


# In[14]:


# Palindrome program without converting to integer number to string
def palindrome(num):
    if num<0:
        return False
    number=num
    n = 0
    while num:
        n = n*10+(num%10)
        num/=10
    
    if n==number:
        return True
    return False

num = input("Enter a number: ")
palindrome(num)


# In[ ]:




