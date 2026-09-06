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


#optimal Solution->Binary Search
class Solution(object):
    def mySqrt(self, x):
        if x==0:
            return 0
        l=1
        r=x
        ans=1
        while l<=r:
            mid=(l+r)//2
            if mid*mid <= x:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
    