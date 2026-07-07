#Solution 1
lst=[1,2,3,4,5]
l=len(lst)-1
left=0
right=l
def reverse(left,right,lst):
    if left>right:
        return
    
    else:
        lst[left],lst[right]=lst[right],lst[left]
    reverse(left+1,right-1,lst)
    return lst
print(reverse(left,right,lst))

#Solution 2
class Solution:
    def reverseArray(self, arr):
        left=0
        right=len(arr)-1
        def rev(left,right,arr):
            if left>right:
                return
            
          
            arr[left],arr[right]=arr[right],arr[left]
            rev(left+1,right-1,arr)
        rev(left,right,arr)
        
        return arr
    
