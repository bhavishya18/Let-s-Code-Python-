#!/usr/bin/env python
# coding: utf-8

# In[6]:


class ListNode:
    def __init__(self, x):
        self.val=x
        self.next=None
class Solution():
    def __init__(self):
        self.head=None
    def append(self, data):
        new_node=ListNode(data)
        if self.head==None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def display(self):
        temp=self.head
        while temp:
            if temp.next==None:
                print temp.val
                return
            print temp.val,'->',
            temp=temp.next
    def removeDups(self,linkedlist):
        head = linkedlist
        temp = head
        while temp.next:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
            
l1=Solution()
l1.append(1)
l1.append(1)
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(3)
l1.append(3)
l1.append(3)
l1.append(9)
l1.append(9)
l1.display()
l2=Solution()
r=ListNode(0)
r.next=l2.removeDups(l1.head)
r=r.next
while r:
    print r.val
    r=r.next


# In[ ]:




