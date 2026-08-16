class Solution:
    def upperBound(self, arr, target):
        # code here
        n=len(arr)-1
        left=0
        right=n
        ub=0
        if target>arr[n]:
            return n+1
            
        while left<=right:
            mid=(left+right)//2
            if arr[mid]>target:
                ub=mid
                right=mid-1
            else:
                left=mid+1
        return ub
'''
TC=o( log n)
SC=o(1)
'''