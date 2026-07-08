#1. Solution

'''
class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)-1
        arr=sorted(arr)
        lar=arr[n]
        sec_lar=-1
        for i in range(n-1,-1,-1):
            if arr[i]>sec_lar and arr[i] != lar:
                sec_lar=arr[i]
        return sec_lar
'''
'''
TC=o(NlogN)+ o(n)
SC=o(1)
'''
#Solution 2