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
