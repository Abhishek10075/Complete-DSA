#Solution 1->Brute
class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        n=len(arr)-1
        maxi=float('-inf')
        for i in range(0,n+1):
            sum=0
            for j in range(i,n+1):
                sum+=arr[j]
                maxi=max(maxi,sum)
        return maxi
'''
TC=o(n*n)
SC=o(1)
'''

#Solution 2->optimal(Kadane's Algorithm)
class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)-1
       
        max_sum=float('-inf')
        cur_sum=0
        for i in range(0,n+1):
            cur_sum=cur_sum+nums[i]
            max_sum=max(cur_sum,max_sum)
            if cur_sum<0:
                cur_sum=0
    
        return max_sum
        
'''
TC=o(n)
SC=o(1)
'''