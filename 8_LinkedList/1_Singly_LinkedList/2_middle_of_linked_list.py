#Find the middle of a linked list
#Solution 1->Brute
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        temp=head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        curr=head
        for i in range(0,count//2):
            head=head.next
        return head
'''
Tc=o(n)+o(n/2)=o(n)
Sc=o(1)
'''

#Solution 2->Optimal
class Solution(object):
    def middleNode(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
'''
TC=o(n/2)=o(n)
SC=o(1)
'''