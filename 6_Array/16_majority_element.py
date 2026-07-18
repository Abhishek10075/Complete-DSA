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

#Solution 2->Better
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
    