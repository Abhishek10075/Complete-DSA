#1 SOlution
'''
sort the arra
return the arr[n-1]
TC-o(N log N)-Because sorting
'''
# Solution

class Solution:
    def largest(self, arr):
        l=len(arr)-1
        largest=arr[0]
        for i in range(0,l+1):
           if arr[i]>largest:
               largest=arr[i]
        return largest
'''
TC=o(N)
SC=o(1)
'''