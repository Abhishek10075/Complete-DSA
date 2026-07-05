class Solution:
    def armstrongNumber (self, n):
        # code here 
        org_num=n
        sum=0
        while n>0:
            r=n%10
            sum=r*r*r+sum
            n=n//10
        if sum==org_num:
            return True
        else:
            return False
        
obj=Solution()  
print(obj.armstrongNumber(153))

'''
TC=O(log₁₀ n)
SC=O(1)
o/p->True
'''