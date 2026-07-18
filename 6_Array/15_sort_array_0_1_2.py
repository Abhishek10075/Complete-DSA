#Solution 1 ->Brute
class Solution:
    def sort012(self, arr):
        arr.sort()
        return arr

'''
TC = O(n log n)
SC = O(1)   # (Ignoring Timsort's internal auxiliary space)

'''

#Solution 2->Better
class Solution:
    def sort012(self, arr):
        n = len(arr)

        z = o = t = 0

        for i in range(n):
            if arr[i] == 0:
                z += 1
            elif arr[i] == 1:
                o += 1
            else:
                t += 1

        for i in range(z):
            arr[i] = 0

        for i in range(z, z + o):
            arr[i] = 1

        for i in range(z + o, n):
            arr[i] = 2

        return arr

'''
TC=O(2n)->o(n)
SC=O(1)
'''