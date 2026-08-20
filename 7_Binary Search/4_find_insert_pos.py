#Find insert postion 
class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)-1
        l=0
        r=n
        pos=n
        if target>nums[n]:
            return n+1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                pos=mid
                r=mid-1
            else:
                l=mid+1
        return pos

'''
TC=o(log n)
SC=o(1)
'''