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
    