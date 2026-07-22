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
        