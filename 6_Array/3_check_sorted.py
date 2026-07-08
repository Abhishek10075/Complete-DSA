#Check array sorted or not
class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        n=len(arr)-1
        if n==0:
            return True
        for i in range(1,n+1):
            if arr[i]>=arr[i-1]:
                continue
            else:
                return False
        return True
        
        
        