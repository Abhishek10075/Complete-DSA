
#Cycle Length in Linked List
class Solution:
    def lengthOfLoop(self, head):
        #code here
        temp=head
        hash_map={}
        count=0
        while temp is not None:
            if temp in hash_map:
                return count - hash_map[temp]
            elif temp not in hash_map:
                hash_map[temp]=count
                count+=1
                temp=temp.next
        return 0

#optimal solution
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                slow=slow.next
                count=1
                while slow!=fast:
                    slow=slow.next
                    count+=1
                return count
        return 0
                    
            