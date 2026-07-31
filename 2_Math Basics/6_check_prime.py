'''
Solution 1

class Solution:
    def isPrime(self, n):
        # code here
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
            else:
                continue
        if count==2:
            return True
        else:
            False
obj=Solution()
print(obj.isPrime(7))
'''

#Solution 2
'''
class Solution:
    def isPrime(self, n):
        # code here
        if n==1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
obj=Solution()
print(obj.isPrime(29))

wors case TC=O(n)  
best cas Tc=O(1)
SC=O(1)

'''

#Solution 3

from math import sqrt
class Solution:
    def isPrime(self, n):
        # code here
        count=0
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                count+=1
                if n//i !=i:
                    count+=1
        if count==2:
            return True
        else:
            return False
        
obj=Solution()
print(obj.isPrime(29))

'''
TC=O(√n)
SC=O(1)
'''