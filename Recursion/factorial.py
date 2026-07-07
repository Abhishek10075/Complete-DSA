class Solution:
    def factorial(self, n: int) -> int:
        # code here
        if n<0:
            return 1
        elif n==0 or n==1:
            return 1
        else:
            return n*(self.factorial)(n-1)
            
obj=Solution()
print(obj.factorial(4))

'''
TC->o(n)
'''