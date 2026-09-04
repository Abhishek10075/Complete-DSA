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
#optimal solution->Binary Search
class Solution:
    def findKRotation(self, arr):
        # code here
        n=len(arr)-1
        l=0
        r=n
        mini=float('inf')
        while l<=r:
            if arr[l]<=arr[r]:
                if arr[l]<=mini:
                    mini=arr[l]
                    index=l
            mid=(l+r)//2
            
            if arr[mid]<=mini:
                mini=arr[mid]
                index=mid
            if arr[mid]>=arr[l]:
                l=mid+1
            else:
                r=mid-1
            
        return index