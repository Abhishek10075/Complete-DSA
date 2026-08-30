#Find K Rotation in a Sorted Rotated Array-Brute Force
class Solution:
    def findKRotation(self, arr):
        n = len(arr) - 1
        break_point = -1

        for i in range(0, n):
            if arr[i] > arr[i + 1]:
                break_point = i
                break

        return break_point + 1
