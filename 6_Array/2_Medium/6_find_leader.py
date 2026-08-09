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
    def leaders(self, arr):
        n=len(arr)-1
        max_el=float('-inf')
        lead=[]
        for i in range(n,-1,-1):
            if arr[i]>=max_el:
                lead.append(arr[i])
                max_el=arr[i]
        n2=len(lead)-1
        left=0
        right=n2
        while left<=right:
            lead[left],lead[right]=lead[right],lead[left]
            left+=1
            right-=1
        
        return lead
'''
TC=O(n)+O(n/2)
SC=O(n)
'''