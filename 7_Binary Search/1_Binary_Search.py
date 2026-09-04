class Solution(object):
    def search(self, nums, target):
        n=len(nums)-1
        low=0
        high=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
'''
TC=o(n/2)
SC=o(1)
'''


