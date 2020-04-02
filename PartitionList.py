#!/usr/bin/env python
# coding: utf-8

# In[14]:


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
    def partitionlist(self, linkedlist, value):
        BeforeList=ListNode(0)
        AfterList = ListNode(0)
        startbefore=BeforeList
        lastbefore=BeforeList
        startafter=AfterList
        lastafter=AfterList
        temp = linkedlist
        while temp:
            if temp.val < value:
                lastbefore.next=ListNode(temp.val)
                lastbefore=lastbefore.next
            else:
                lastafter.next=ListNode(temp.val)
                lastafter=lastafter.next
            temp=temp.next
        startbefore=startbefore.next
        startafter=startafter.next
        lastbefore.next=startafter
        return startbefore
        
            
l1=Solution()
l1.append(1)
l1.append(4)
l1.append(3)
l1.append(2)
l1.append(5)
l1.append(2)
l1.display()
l2 = Solution()
r=ListNode(0)
value=3
r.next=l2.partitionlist(l1.head,value)
r=r.next
while r:
    if r.next==None:
        print r.val
        break
    print r.val,'->',
    r=r.next


# In[ ]:




