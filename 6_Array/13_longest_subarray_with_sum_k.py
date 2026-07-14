# #Solution 1
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
    
# '''
# TC=o(N*N)
# SC=o(1)
# '''

#Solution 2->optimal

# Solution 2 -> optimal
arr = [1,2,3,1,1,1,1,3,3]
k = 6
n = len(arr) - 1

sum = 0
i, j = 0, 0
max_l = 0

while j < n + 1:
    sum = sum + arr[j]

    if sum < k:
        j = j + 1

    elif sum == k:
        l = j - i + 1
        max_l = max(max_l, l)
        j = j + 1

    elif sum > k:
        while sum > k and i <= j:
            sum = sum - arr[i]
            i = i + 1

        if sum == k:
            l = j - i + 1
            max_l = max(max_l, l)

        j = j + 1

print(max_l)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''