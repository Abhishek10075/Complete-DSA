#Count the prime number
'''
204. Count Primes
premium lock icon
Companies
Hint
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
'''
from math import sqrt
class Solution(object):
    def checkPrime(self,n):
        count=0
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                count+=1
                if n//i!=i:
                    count+=1
        if count==2:
            return True
        else: 
            return False

    def countPrimes(self, n):
        count_prime=0
        for i in range(1,n):
            if self.checkPrime(i):
                count_prime+=1
        return count_prime
    