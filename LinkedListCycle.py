#!/usr/bin/env python
# coding: utf-8

# In[7]:


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
    def ListCycle(self,head):
        
        ourlist=head
        slow=head
        fast=head
        if slow==None or slow.next==None:
            return False
        while True:
            slow=slow.next
            fast=fast.next.next
            if slow==None or slow.next==None or fast==None or fast.next==None:
                return False
            if slow==fast:
                break
        slow=ourlist
        if slow==fast:
            return True
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        if slow==fast:
            return True
l1 = Solution()
l1.append(3)
l1.append(2)

l1.append(0)
l1.append(-4)
l1.append(2)
l1.display()
r=Solution()
r.ListCycle(l1.head)


# In[ ]:




