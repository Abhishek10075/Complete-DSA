#Find Minimum in Rotated Sorted Array->Brute Force
class Solution(object):
    def findMin(self, nums):
        n=len(nums)-1
        mini=float('inf')
        for i in range(0,n+1):
            if nums[i]<mini:
                mini=nums[i]
        return mini

#Optimal solution->Binary Search
class Solution(object):
    def findMin(self, nums):
        n = len(nums) - 1
        mini = float('inf')
        l = 0
        r = n

        while l <= r:
            mid = (l + r) // 2

            # Left part is sorted
            if nums[l] <= nums[mid]:
                mini = min(mini, nums[l])
                l = mid + 1

            # Right part is sorted
            else:
                mini = min(mini, nums[mid])
                r = mid - 1

        return mini
    