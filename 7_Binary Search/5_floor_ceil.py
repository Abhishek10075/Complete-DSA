#Find only flor
class Solution:
    def findFloor(self, arr, x):
        l = 0
        r = len(arr) - 1
        floor = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= x:
                floor = mid      # <-- save this as a candidate before moving right
                l = mid + 1
            else:
                r = mid - 1
        return floor

#Find only ceil
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
#Find Flor and Ceil

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
    