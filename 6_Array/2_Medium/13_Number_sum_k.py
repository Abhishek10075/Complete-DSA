#Count subarray sum Equals k
#Brute
class Solution(object):
    def subarraySum(self, nums, k):
        n=len(nums)-1
        count=0
        maxi=0
        for i in range(0,n+1):
            sum=0
            for j in range(i,n+1):
                sum=sum+nums[j]
                if sum==k:
                    count+=1
            
        return count

'''
TC=o(N*N)
SC=o(1)
'''