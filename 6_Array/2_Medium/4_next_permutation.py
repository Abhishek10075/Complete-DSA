#Solutin ->optimal 

class Solution:
    def reverse(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    def nextPermutation(self, arr):
        n = len(arr) - 1
        ind = -1

        # Step 1: Find the breakpoint
        for i in range(n - 1, -1, -1):
            if arr[i] < arr[i + 1]:
                ind = i
                break

        # Step 2: If no breakpoint, reverse entire array
        if ind == -1:
            self.reverse(arr, 0, n)
            return arr

        # Step 3: Find the next greater element from the right
        for j in range(n, ind, -1):
            if arr[j] > arr[ind]:
                arr[j], arr[ind] = arr[ind], arr[j]
                break

        # Step 4: Reverse the remaining suffix
        self.reverse(arr, ind + 1, n)

        return arr
    
'''
TC=O(N) + O(N) + O(N)= O(3N)= O(N)
SC=O(N)

'''