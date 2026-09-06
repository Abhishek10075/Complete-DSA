#Brute Force solution 
class Solution(object):
    def mySqrt(self, x):
        if x==0:
            return 0
        
        for i in range(1,int(x//2)+2):
            if i*i==x:
                return i
            elif i*i<x:
                continue
            else:
                return i-1


        