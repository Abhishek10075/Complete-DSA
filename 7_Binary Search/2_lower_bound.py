#Find lowerbound 
class Solution:
    def lowerBound(self, arr, target):
        n=len(arr)
    
        l=0
        r=n-1
        lb=n
        while  l<=r:
            mid=(l+r)//2
            if arr[mid]>=target:
                lb=mid
                r=mid-1
            else:
                l=mid+1
               
        return lb

''' 
Time Complexity  : O(log n)
Space Complexity : O(1)
'''