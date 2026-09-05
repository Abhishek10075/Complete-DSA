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
            
        
        