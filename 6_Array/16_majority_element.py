#Solution 1->Brute
class Solution:
    def majorityElement(self, arr):
        #code here
        n=len(arr)
        for i in range(0,n):
            count=0
            for j in range(0,n):
                if arr[i]==arr[j]:
                    count+=1
                    
            if count>n//2:
                return arr[i]
        return -1
        
'''
 TC=o(n*n)
 SC=o(1)
 '''  

#Solution 2->Better using sorting
class Solution:
    def majorityElement(self, arr):
        #code here
        arr.sort()
        n=len(arr)
        if n==1:
            return arr[0]
        count=1
        ans=arr[0]
        for i in range(1,n):
            if arr[i]==ans:
                count+=1
                if count>n//2:
                    return ans
            elif arr[i]!=ans:
                ans=arr[i]
                count=1
        return -1
                
'''
TC=O(n log n)+o(n)
SC=o(1)
'''              

#Solution 3->Better
class Solution:
    def majorityElement(self, arr):
        #code here
        n = len(arr)
        hashmap={}
        for i in arr:
            if i not in hashmap:
                hashmap[i]=1
            elif i in hashmap:
                hashmap[i]+=1
        for k,v in hashmap.items():
            if v>n//2:
                return k
        return -1
        

'''
TC=o(n)
SC=o(n)
'''
    
#Solution 4 ->Optimal 
class Solution:
    def majorityElement(self, arr):
        n = len(arr)

        majority = None
        count = 0

        # Phase 1: Find the potential majority element
        for element in arr:
            if count == 0:
                majority = element
                count = 1
            elif element == majority:
                count += 1
            else:
                count -= 1

        # Phase 2: Verify that it is actually the majority
        count = 0
        for element in arr:
            if element == majority:
                count += 1

        if count > n // 2:
            return majority

        return -1