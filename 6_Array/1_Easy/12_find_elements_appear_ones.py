#Solution 1-Brute 

class Solution:
    def findUnique(self, arr):
        # code here 
        n=len(arr)-1
        for i in range(0,n+1):
            count=0
            for j in range(0,n+1):
                if arr[j]==arr[i]:
                    count+=1
            if count==1:
                return arr[i]
'''
TC=o(N*N)
SC=o(1)
'''

#Solution 2 -Better usign hashing

class Solution(object):
    def singleNumber(self, nums):
        n=len(nums)-1
        f={}
        for i in range(0,n+1):
            if nums[i] not in f:
                f[nums[i]]=1
            elif nums[i] in f:
                f[nums[i]]+=1
        for k,v in f.items():
            if v==1:
                return k

     
        
'''
TC=o(2N)
SC=o(N)
'''

#optimal solution
class Solution:
    def findUnique(self, arr):
        ans = 0

        for num in arr:
            ans ^= num

        return ans
'''
TC=o(n)
SC=o(1)
'''