#Find insert postion 
class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)-1
        left=0
        right=n
        index=0
        if target<nums[0]:
            return 0
        if target>nums[n]:
            return n+1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                index=mid
                right=mid-1
            else:
                left=mid+1
        return index
'''
TC=o(log n)
SC=o(1)
'''