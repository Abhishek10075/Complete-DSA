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
