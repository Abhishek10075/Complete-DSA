#Solution 1->Brute
class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)-1
        m=0
        n=len(nums)-1
    
        for i in range(0,n+1):
            num=nums[i]
            count=1
            while num+1 in nums:
                count+=1
                num+=1
            m=max(m,count)
        return m


'''
TC=o(n*n)
sc=o(1)
'''