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
class Solution:
    def gcd(self, a, b):
        gcd = 1
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                gcd = i
        return gcd

# '''

# ([1, 3, 5, 15], [1, 2, 3, 6, 9, 18], 3)
# TC=O(√a + √b + k log k)
# SC=O(k) //where k is the number of divisors.
# '''          

#leet code 
class Solution(object):
    def findGCD(self, nums):
        smaller=nums[0]
        for i in range(0,len(nums)):
            if nums[i]<smaller:
                smaller=nums[i]
        larger=nums[0]
        for j in range(0,len(nums)):
            if nums[j]>larger:
                larger=nums[j]
        
        for i in range(1,smaller+1):
            if smaller%i==0 and larger%i==0:
                gcd=i
        return gcd
    

   
