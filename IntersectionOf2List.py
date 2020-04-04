#!/usr/bin/env python
# coding: utf-8

# In[11]:


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
    def intersectList(self,l1,l2):
        if l1==None and l2==None:
            return None
        count1=1
        count2=1
        trav1=l1
        trav2=l2
        while trav1.next:
            count1+=1
            trav1=trav1.next
        while trav2.next:
            count2+=1
            trav2=trav2.next
      
        if trav1!=trav2:
            return False
        print count1
        print count2
        trav1=l1
        trav2=l2
        count=0
        if count1>count2:
            count=count1-count2
            temp=0
            while temp<count:
                trav1=trav1.next
                temp+=1
        elif count1<count2:
            count=count2-count1
            temp=0
            while temp<count:
                trav2=trav2.next
                temp+=1
        while trav1 and trav2:
            if trav1==trav2:
                return trav1.val
            trav1=trav1.next
            trav2=trav2.next
            


# In[ ]:




