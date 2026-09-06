#162. Find Peak Element
class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)-1
        if n==0:
            return 0
        if n==1:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        if nums[0]>nums[1]:
            return 0
        if nums[n]>nums[n-1]:
            return n
            
        for i in range(1,n):
            if nums[i-1] < nums[i]> nums[i+1]:
                return i 
            
#optimal Solution->Binary Search
class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)-1
        l=0
        r=n
        if n==0:
            return 0
        if n==1:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1

        if nums[n]>nums[n-1]:
            return n
        l=1
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid-1] < nums[mid] and nums[mid]> nums[mid+1]:
                return mid
            elif nums[mid-1]<nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return 0
        
        