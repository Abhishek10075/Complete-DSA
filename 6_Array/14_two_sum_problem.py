#Solution 1 ->Brute
# Solution 1 -> Brute Force
class Solution:
    def twoSum(self, arr, target):
        # code here
        n = len(arr) - 1

        for i in range(0, n + 1):
            for j in range(i + 1, n + 1):
                if arr[i] + arr[j] == target:
                    return True   # or [i, j]

        return False

#Solution 2->Better

		  
