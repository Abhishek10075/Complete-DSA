#Program: Count the Number of Subarrays with Sum Equal to K
class Solution(object):
    def subarraySum(self, nums, k):
        n=len(nums)-1
        count=0
        for i in range(0,n+1):
            sum=0
            for j in range(i,n+1):
                sum+=nums[j]
                if sum==k:
                    count+=1
            
        return count


# #Solution 1
class Solution:

    def longestSubarray(self, nums, k):
        n = len(nums)
        max_count = 0

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]

                if s == k:
                    length = j - i + 1
                    max_count = max(max_count, length)

        return max_count
    
'''
TC=o(N*N)
SC=o(1)
 '''





#Prefix sum->optimal solution

arr=[9,4,20,3,10,5]
k=33
n=len(arr)
prefix_sum=0
max_count=0
hashmap={}
for i in range(n):
    prefix_sum+=arr[i]

    if prefix_sum==k:
        max_count=i+1

    rem=prefix_sum-k

    if rem in hashmap:
        length=i-hashmap[rem]
        max_count=max(max_count,length)

    if prefix_sum not in hashmap:
        hashmap[prefix_sum]=i
print("Maximum Length:",max_count)

'''
TC=o(n)
SC=o(1)
'''
    

