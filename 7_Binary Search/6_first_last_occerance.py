#Solution 1 Brute Force
class Solution(object):
    def searchRange(self, nums, target):
        n=len(nums)-1
        first=-1
        last=-1
        for i in range(0,n+1):
            if nums[i]==target:
                if first==-1:
                    first=i
                last=i
        return [first,last]

#second method 
class Solution:
    def find(self, arr, x):
        # code here
        n=len(arr)-1
        first=-1
        last=-1
        for i in range(0,n+1):
            if arr[i]==x and first==-1:
                first=i
            if arr[i]==x:
                last=i
        return [first,last]


#optimal solution 

class Solution(object):
    def lowerbound(self, nums, target):
        l = 0
        r = len(nums) - 1
        lb = len(nums)

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                lb = mid
                r = mid - 1
            else:
                l = mid + 1

        return lb

    def upperbound(self, nums, target):
        l = 0
        r = len(nums) - 1
        ub = len(nums)

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                ub = mid
                r = mid - 1
            else:
                l = mid + 1

        return ub

    def searchRange(self, nums, target):
        lower = self.lowerbound(nums, target)

        # Target does not exist
        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]

        upper = self.upperbound(nums, target)

        return [lower, upper - 1]