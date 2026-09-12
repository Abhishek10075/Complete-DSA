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

#Optimal Solutions

class Solution:
    def rev(self,arr,l,r):
        n=len(arr)-1
        l=0
        r=n
        while l<=r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        return arr
        
    def leaders(self, arr):
        # code here
        n=len(arr)-1
        lead=[]
        maxi=float('-inf')
        for i in range(n,-1,-1):
            if arr[i]>=maxi:
                maxi=arr[i]
                lead.append(arr[i])
            else:
                continue
        n=len(arr)-1
        l=0
        lead=self.rev(lead,l,n)
        return lead
            
            
            
'''
TC=O(n)+O(n/2)
SC=O(n)
'''