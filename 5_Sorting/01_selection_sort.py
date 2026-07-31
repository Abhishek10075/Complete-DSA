class Solution: 
    def selectionSort(self, arr):
        # code here
        n=len(arr)-1
        for i in range(0,n+1):
            for j in range(i+1,n+1):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr
'''
TC=o(N*N)
SC=o(1)
'''