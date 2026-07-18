#Program: Count the Number of Subarrays with Sum Equal to K
# class Solution(object):
#     def subarraySum(self, nums, k):
#         n=len(nums)-1
#         count=0
#         for i in range(0,n+1):
#             sum=0
#             for j in range(i,n+1):
#                 sum+=nums[j]
#                 if sum==k:
#                     count+=1
            
#         return count


# # #Solution 1
# class Solution:

#     def longestSubarray(self, nums, k):
#         n = len(nums)
#         max_len = 0

#         for i in range(n):
#             s = 0
#             for j in range(i, n):
#                 s += nums[j]

#                 if s == k:
#                     length = j - i + 1
#                     max_len = max(max_len, length)

#         return max_len
    
# # '''
# # TC=o(N*N)
# # SC=o(1)
# # '''

# # Solution 2 -> optimal
# arr = [1,2,3,1,1,1,1,3,3]
# k = 6
# n = len(arr) - 1

# sum = 0
# i, j = 0, 0
# max_l = 0

# while j < n + 1:
#     sum = sum + arr[j]

#     if sum < k:
#         j = j + 1

#     elif sum == k:
#         l = j - i + 1
#         max_l = max(max_l, l)
#         j = j + 1

#     elif sum > k:
#         while sum > k and i <= j:
#             sum = sum - arr[i]
#             i = i + 1

#         if sum == k:
#             l = j - i + 1
#             max_l = max(max_l, l)

#         j = j + 1

# print(max_l)

# '''
# Time Complexity: O(n)
# Space Complexity: O(1)
# '''

