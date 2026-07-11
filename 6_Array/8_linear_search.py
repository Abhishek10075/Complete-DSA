#Solution 1->Using while loop
class Solution:
    def search(self, arr, x):
        # code here
        n=len(arr)-1
        i=0
        while i<n+1:
            if arr[i]==x:
                return i
            i+=1
        if i==n+1:
            return -1
        
#Solution 2->Using for loop
class Solution:
    def search(self, arr, x):
        # code here
        n=len(arr)-1
        for i in range(0,n+1):
            if arr[i]==x:
                return i
        return -1
                
        
                