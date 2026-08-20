#Find upper bound optimal solution
class Solution:
    def upperBound(self, arr, target):
        # code here
        n=len(arr)
        l=0
        r=n-1
        ub=n
        while l<=r:
            mid=(l+r)//2
            if arr[mid]>target:
                ub=mid
                r=mid-1
            else:
                l=mid+1
        return ub

'''
TC=o( log n)
SC=o(1)
'''