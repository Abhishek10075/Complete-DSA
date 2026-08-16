#Find lowerbound 
class Solution:
    def lowerBound(self, arr, target):
        # code here
        n=len(arr)-1
        l=0
        r=n
        lb=0
        if target<arr[0]:
            return 0
        if target>arr[n]:
            return n+1
        while l<=r:
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