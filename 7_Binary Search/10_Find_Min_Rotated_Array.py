#Find Minimum in Rotated Sorted Array
class Solution(object):
    def findMin(self, nums):
        n = len(nums) - 1
        l = 0
        r = n

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]