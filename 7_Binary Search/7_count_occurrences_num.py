#Number of Occurrence-Brute Force
class Solution:
    def countFreq(self, arr, target):
        # code here
        n=len(arr)-1
        first=-1
        last=-1
        for i in range(0,n+1):
            if arr[i]==target:
                if first==-1:
                    first=i
                last=i
        if first==-1:
            return 0
            
        else:
            return last-first+1


#Optimal Solution
class Solution:
    def lowerbound(self,arr,target):
        n=len(arr)
        l=0
        r=n-1
        lb=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]>=target:
                lb=mid
                r=mid-1
            else:
                l=mid+1
        return lb
        
    def upperbound(self,arr,target):
        n=len(arr)
        l=0
        r=n-1
        ub=n #when target is greater than all elements in the array
        while l<=r:
            mid=(l+r)//2
            if arr[mid]>target:
                ub=mid
                r=mid-1
            else:
                l=mid+1
        return ub
        
    def countFreq(self, arr, target):
        # code here
        n=len(arr)-1
        lower=self.lowerbound(arr,target)
        if lower==-1:
            return 0
        upper=self.upperbound(arr,target)
        
        return upper-lower

    