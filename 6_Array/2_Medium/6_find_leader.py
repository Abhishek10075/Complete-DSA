#Solution 1->Brute
class Solution:
    def leaders(self, arr):
        # code here
        n=len(arr)-1
        leaders=[]
        for i in range(0,n+1):
            lead=True
            for j in range(i+1,n+1):
                if arr[j]>arr[i]:
                    lead=False
            if lead:
                leaders.append(arr[i])
               
        return leaders
#second logic
class Solution:
    def leaders(self, arr):
        # code here
        n=len(arr)-1
        leaders=[]
        for i in range(0,n+1):
            lead=arr[i]
            for j in range(i+1,n+1):
                if arr[i]>=arr[j]:
                    if j==n:
                        leaders.append(arr[i])
                else:
                    break
        leaders.append(arr[n])
                   
               
        return leaders
''''
TC=o(n)
SC=o(n)
'''