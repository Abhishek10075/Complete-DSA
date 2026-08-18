#ceil means greater than or equal to the given number
'''
example: arr=[1,2,8,10,10,12,19], x=5
output: 2 (index of 8)
because 8 is the smallest number which is greater than or equal to 5
TC=o(log n)
SC=o(1)
'''
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

