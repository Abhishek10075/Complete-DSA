#Using the while loop
class Solution:
    def isPalindrome(self, s):
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left=left+1
            right=right-1
        return True

#Using the Recursion
class Solution:
    def isPalindrome(self, s):
        left=0
        right=len(s)-1
        def checkPalindrome(left,right,s):
            
            if left>=right:
                return True
                
            elif s[left]!=s[right]:
                return False
            
            else:
                return checkPalindrome(left+1,right-1,s)
        return  checkPalindrome(left,right,s)
            
            
        

         
            
        

