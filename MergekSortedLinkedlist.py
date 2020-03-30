#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Queue import PriorityQueue
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
    def mergekList(self,list):
        q = PriorityQueue()
        result = temp = ListNode(0)
        for i in list:
            if i:
                q.put((i.val, i))
                
        while q:
            key, node = q.get()
            temp.next = ListNode(key)
            temp=temp.next
            node = node.next
            if node:
                q.put((node.val, node))
        out = []
        while result:
            out.append(result.val)
            result=result.next
        print out
    
l1 = Solution()
l1.append(1)
l1.append(4)
l1.append(5)
l2 = Solution()
l2.append(1)
l2.append(3)
l2.append(4)
l3 = Solution()
l3.append(2)
l3.append(6)

l4 = []
l4.append(l1.head)
l4.append(l2.head)
l4.append(l3.head)

r=Solution()
result = r.mergekList(l4)
out = []
while result:
    out.append(result.val)
    result=result.next
print out


# In[ ]:




