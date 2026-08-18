class Solution:
    def findCeil(self, arr, x):
        # code here
        n=len(arr)-1
        l=0
        r=n
        ceil=-1
        while l<=r:
            mid=(l+r)//2

            if arr[mid]>=x:
                ceil=mid
                r=mid-1
            else:
                l=mid+1
        return ceil

