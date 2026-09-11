#Solution 1 ->Brute
class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)-1
        maxi=0
        for i in nums:#o(n)
            count=1
            num=i
            while num+1 in nums:#o(n)
                count+=1
                num=num+1
            maxi=max(count,maxi)
        return maxi
'''
TC=o(n*n)
SC=o(1)
'''

#Better using sorting method
class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        n=len(nums)-1
        last_smaller=float('-inf')
        longest=0
        count=0
        if n==0:
            return 1
        for i in range(0,n+1):
            if count==0:
                last_smaller=nums[i]
                count=1
            if nums[i]==nums[i-1]+1:
                count+=1
                longest=max(longest,count)
            elif nums[i]==nums[i-1]:
                longest=max(longest,count)
                continue
            elif nums[i]!=nums[i-1]:
                last_smaller=nums[i]
                count=1
            longest=max(longest,count)
        return longest
            

        
