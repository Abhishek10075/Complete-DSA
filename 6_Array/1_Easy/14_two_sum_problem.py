# Solution 1 -> Brute
class Solution:
    def twoSum(self, arr, target):
        # code here
        n = len(arr) - 1

        for i in range(0, n + 1):
            for j in range(i + 1, n + 1):
                if arr[i] + arr[j] == target:
                    return True   # or [i, j]

        return False
'''
TC=o(N*N)
SC=o(N)
'''

#Solution 2->Better
		  
class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)-1
        hashmap={}
        for i in range(0,n+1):
            reamaining=target-nums[i]
            if  reamaining in hashmap:
                return [hashmap[ reamaining],i]
            hashmap[nums[i]]=i
'''
TC=o(n)
SC=o(n)
'''

#Solution 3->optimal (If array is sorted)
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

'''
TC=o(n)
SC=o(1)
'''