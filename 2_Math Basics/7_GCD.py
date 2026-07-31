from math import sqrt
class Solution:
    def gcd(self, a, b):
        def cal_fact(num):
            factors=[]
            for i in range(1,int(sqrt(num))+1):
                if num%i==0:
                    factors.append(i)
                    
                    if num//i !=i:
                        factors.append(num//i)
                else:
                    continue
            return factors
        a_fact=sorted(cal_fact(a))
        b_fact=sorted(cal_fact(b))
        largest=1
        for i in range(0,len(b_fact)):
            for j in range(0,len(a_fact)):
                if b_fact[i]==a_fact[j]:
                    largest=b_fact[i]
                else:
                    continue

        return a_fact, b_fact, largest
obj=Solution()
print(obj.gcd(11,13))

#method 2
from math import sqrt

class Solution:
    def gcd(self, a, b):
        for i in range(1, min(a,b)+1):
            if a%i==0 and b%i==0:
                gcd=i
        return gcd
            
'''
([1, 3, 5, 15], [1, 2, 3, 6, 9, 18], 3)
TC=O(√a + √b + k log k)
SC=O(k) //where k is the number of divisors.
'''          
        
