# Linked List Cycle
#Brute Force Approach 
class Solution(object):
    def hasCycle(self, head):
        temp=head
        myset=set()
        while temp is not None:
            if temp in myset:
                return True
            else:
                myset.add(temp)
                temp=temp.next
        return False

#optimal Solution
class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True

        return False

