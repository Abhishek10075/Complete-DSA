class Solution(object):
    def reverseList(self, head):
        prev=None
        temp=head
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
            
        return prev
        