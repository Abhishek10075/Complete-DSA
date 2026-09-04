#Find the single element in sorted array.
class Solution(object):
    def singleNonDuplicate(self, nums):
        for i in range(0,len(nums)-1,2):
            if nums[i]!=nums[i+1]:
                return nums[i]
        return nums[-1]

#Better
class Solution(object):
    def singleNonDuplicate(self, nums):
        n=len(nums)-1
        l=0
        r=n
        if n==0:
            return nums[0]
        while l<=r:
            if nums[l]!=nums[l+1]:
                return nums[l]
            if nums[r]!=nums[r-1]:
                return nums[r]
            l+=2
            r-=2
'''
TC=o(n/4)
SC=o(1)
'''

#Optimal Solution->Binary Search
class Solution(object):
    def singleNonDuplicate(self, nums):
        n=len(nums)-1
        l=0
        r=n
        if n==0:
            return nums[0]
        while l<=r:
            mid=(l+r)//2
            if mid==0 and nums[0] !=nums[1]:
                return nums[mid]

            if mid==n and nums[n]!=nums[n-1]:
                return nums[mid]
                
            if mid!=0 and mid!=n:
                if nums[mid-1]!=nums[mid]!=nums[mid+1]:
                    return nums[mid]
                    break
            
            if mid%2==0:
                if nums[mid]==nums[mid-1]:
                    r=mid-1
                elif nums[mid]==nums[mid+1]:
                    l=mid+1
            
            elif mid%2 !=0:
                if nums[mid]==nums[mid-1]:
                    l=mid+1
                elif nums[mid]==nums[mid+1]:
                    r=mid-1