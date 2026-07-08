class Solution(object):
    def reverse(self, x):
        rev=0
        sign=1
        if x<0:
            sign=-1
            x=x*-1
        else:
            x=x
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        result=sign*rev
        if result < -2147483648 or result > 2147483648:
            return 0
        
        return result
       
obj=Solution()
print(obj.reverse(-123))

'''
TC=O(log₁₀ n)
SC=O(1)
o/p->-321
'''