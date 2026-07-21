# Solution 1 -> Brute

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        for i in range(k):
            last_el = nums.pop()
            nums.insert(0, last_el)

'''
Time Complexity: O(k * n)
Space Complexity: O(1)
'''


# Solution 2 -> Using Slicing

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        nums[:] = nums[n-k:] + nums[:n-k]

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''


# Solution 3 -> Optimal (Reversal Algorithm)

class Solution(object):
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, 0, n-1)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''