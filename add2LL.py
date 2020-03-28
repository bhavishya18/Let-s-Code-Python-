#!/usr/bin/env python
# coding: utf-8

# In[2]:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head= None
        
    def append(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head= new_node
        
    def display(self):
        temp = self.head
        while temp:
            if temp.next == None:
                print temp.val,
            else:
                print temp.val, "->",
            
            temp=temp.next
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        carry = 0
        head=l3
        while(l1 or l2 ):
            if not l1:
                x=0
            else:
                x=l1.val
            if not l2:
                y=0
            else:
                y=l2.val
            sum=x+y+carry
            if sum>9:
                carry=1
                sum=sum%10
            else:
                carry=0
            head.next=ListNode(sum)
            head=head.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2=l2.next
            
        if carry==1:
            head.next=ListNode(carry)
        return l3.next
            
          
l1 = Solution()
l2 = Solution()

num1= input("Enter List 1:")
num1= str(num1)
num2= input("Enter List 2:")
num2= str(num2)
for i in num1:
    l1.append(int(i))
for i in num2:
    l2.append(int(i))


print "\nInput:"
print "(",
l1.display(),
print ") ",
print "+ " ,
print "(",
l2.display(),
print ")"
result = Solution().addTwoNumbers(l1.head, l2.head)
print "\nSum of two numbers is"
while result:
    if result.next == None:
        print result.val,
    else:
        print result.val, "->",
    result = result.next


# In[ ]:




