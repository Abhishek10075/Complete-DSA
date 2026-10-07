'''
Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low = 0
        high = len(letters) - 1

        while low <= high:
            mid = (low + high) // 2

            if letters[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return letters[low % len(letters)]
    