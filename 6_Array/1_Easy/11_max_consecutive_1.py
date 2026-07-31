class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)-1
        max_one=0
        count=0
        for i in range(0,n+1):
            if nums[i]==1:
                count+=1
                max_one=max(max_one,count)
            else:
                count=0
        return max_one
    