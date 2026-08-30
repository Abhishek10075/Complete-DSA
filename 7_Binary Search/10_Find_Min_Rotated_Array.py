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
        n=len(nums)-1
        l=0
        r=n
        mini=float('inf')
        while l<=r:
            mid=(l+r)//2
            if nums[l]<=nums[r]:
                mini=min(mini,nums[l])
            mini=min(mini,nums[mid])
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1
        return mini