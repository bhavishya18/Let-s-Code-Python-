#!/usr/bin/env python
# coding: utf-8

# In[6]:


class MyQueue:
    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]
    def push(self, data):
        self.push_stack.append(data)
    def pop(self):
        if self.pop_stack:
            val=self.pop_stack.pop()
            return val
        elif not self.push_stack:
            return None
        else:
            for i in range(0,len(self.push_stack)):
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()
    def peek(self):
        if self.pop_stack:
            
            return self.pop_stack[-1]
        elif not self.push_stack:
            return None
        else:
            for i in range(0,len(self.push_stack)):
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack[-1]
    def empty(self):
        if len(self.push_stack)==0 and len(self.pop_stack)==0:
            return True
        else:
            return False
        

s=MyQueue()
s.push(1)
s.push(2)
print s.peek()
print s.pop()
print s.empty()


# In[ ]:




