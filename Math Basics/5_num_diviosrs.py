
'''
lass Solution:
    def GCD(self, n1, n2):
        def cal_divisor(num):
            d=[]
            for i in range(1,num+1):
                if num%i==0:
                    d.append(i)
                else:
                    continue
            return d
        n1_div=cal_divisor(n1)
        n2_div=cal_divisor(n2)
        lar=1
        for i in range(0, len(n2_div)):
            for j in range(0,len(n1_div)):
                if n2_div[i]==n1_div[j]:
                    lar=n2_div[i]
                else:
                    continue
            
        return lar

obj=Solution()
print(obj.GCD(9,18))       
    
  
'''
from math import sqrt
class Solution:
    def getDivisors(self, n):
        divisors=[]
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                divisors.append(i)
                if n//i !=i:
                    divisors.append(n//i)
        sorted_divisors=sorted(divisors)
        return sorted_divisors
       
obj=Solution()      
print(obj.getDivisors(36))

'''
O(√n + k log k)
SC=O(k) //where k is the number of divisors.
o/p-> [1, 2, 3, 4, 6, 9, 12, 18, 36]
'''