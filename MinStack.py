#!/usr/bin/env python
# coding: utf-8

# In[26]:


class MinStack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
        
    def pop(self):
        
        del self.stack[-1]
         
        
    def top(self):
        return self.stack[-1]
    def getMin(self):
        self.minstack=self.stack
        self.minval=self.minstack[0]
        i=1
        while i<len(self.minstack):
            self.minval=min(self.minval,self.minstack[i])
            i+=1
        return self.minval
    
l = MinStack()
l.push(-2)
l.push(0)
l.push(-3)
print l.getMin()
l.pop()
print l.top()
print l.getMin()


# In[29]:


# Other way of doig this is to maitain one more list that contains min elements
import sys
class MinStack:
    def __init__(self):
        self.stack=[]
#         stack to hold minimum valued elements
        self.minstack=[]
        self.minstack.append(sys.maxint)
        
    def push(self,x):
        self.stack.append(x)
        if x <= self.minstack[-1]:
            self.minstack.append(x)
        
    def pop(self):
        if self.stack[-1]==self.minstack[-1]:
            del self.minstack[-1]
        del self.stack[-1]
         
        
    def top(self):
        return self.stack[-1]
    def getMin(self):
        
        return self.minstack[-1]
    
l = MinStack()
l.push(-2)
l.push(0)
l.push(-3)
print l.getMin()
l.pop()
print l.top()
print l.getMin()


# In[ ]:




