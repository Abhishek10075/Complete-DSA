'''
Solution 1

class Solution:
    def removeDuplicates(self, arr):
        n=len(arr)-1
        f={}
        for i in range(0,n+1):
            if arr[i] not in f:
                f[arr[i]]=0
        j=0
        for k in f:
            arr[j]=k
            j=j+1
        arr=arr[:j]
        return arr
        


Time Complexity: O(n)
Space Complexity: O(n)
'''

#optimal solution

class Solution:
    def removeDuplicates(self, arr):
        if len(arr) == 0:
            return []

        i = 0

        for j in range(1, len(arr)):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
                arr[j]=arr[i]

        return arr[:i + 1]
'''
TC=o(n)
SC=o(1)
'''