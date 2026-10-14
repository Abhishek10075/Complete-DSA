# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        temp=head
        myset=set()
        while temp is not None:
            if temp in myset:
                return temp
                break

            elif temp not in myset:
                myset.add(temp)
                temp=temp.next
        return None
        