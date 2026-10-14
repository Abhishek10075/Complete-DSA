class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        length=0
        while temp is not None:
            length+=1
            temp=temp.next
        if length==n:
            new_head=head.next
            del head
            return new_head
        pos_to_stop=length-n
        temp=head
        count=1
        while count<pos_to_stop:
            temp=temp.next
            count+=1
        temp.next=temp.next.next
        return head
        