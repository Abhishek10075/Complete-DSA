class Solution:
    def getFloorAndCeil(self, nums, x):
        n=len(nums)-1
        l=0
        r=n
        flor=-1
        ceil=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==x:
                return [nums[mid],nums[mid]]
            elif nums[mid]>x:
                ceil=nums[mid]
                r=mid-1
            else:
                floor=nums[mid]
                l=mid+1
        return [floor, ceil]