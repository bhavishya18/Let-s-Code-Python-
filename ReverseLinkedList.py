#!/usr/bin/env python
# coding: utf-8

# In[34]:


class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = ListNode(data)
        if self.head==None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last=last.next
        last.next = new_node
    
    def display(self):
        temp = self.head
        while temp:
            if temp.next==None:
                print temp.val
                return
            print temp.val, '->',
            temp  =temp.next
    def reverseList(self, ll):
        head=ll
        prev=None
        while head:
            curr=ListNode(head.val)
            head=head.next
            curr.next=prev
            prev=curr
            
        print prev
        print curr
        print head
        return prev
    
l=Solution()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.display()
r=Solution()
result=ListNode(0)
result.next=r.reverseList(l.head)
result=result.next
while result:
    print result.val,
    result=result.next


# In[36]:


class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = ListNode(data)
        if self.head==None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last=last.next
        last.next = new_node
    
    def display(self):
        temp = self.head
        while temp:
            if temp.next==None:
                print temp.val
                return
            print temp.val, '->',
            temp  =temp.next
    def reverseList(self, ll):
        if ll==None or ll.next==None:
            return ll
        p=ListNode(self.reverseList(ll.next))
        ll.next.next=ll
        ll.next=None
        return p
    
    
l=Solution()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.display()
r=Solution()
result=ListNode(0)
result.next=r.reverseList(l.head)
result=result.next

while result:
    print result.val,
    result=result.next


# In[ ]:




