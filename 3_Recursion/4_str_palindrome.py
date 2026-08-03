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

'''
TC=o(n/2)->o(n)
'''
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
            
            
        

#check sentence is palindrome or not ->brute solution
class Solution(object):
    def isPalindrome(self, s):
        valid_string=''
        s=s.split()
        s=''.join(s)
        for i in s:
            if i.isalpha() or i.isdigit():
                valid_string+=i
        valid_string=valid_string.lower()
        n=len(valid_string)
        left=0
        right=n-1
        pali=True
        while left<=right:
            if valid_string[left]!=valid_string[right]:
                pali=False
            left+=1
            right-=1
        if pali:
            return True
        else:
            return False
#Palindrome Check (Alphanumeric)
class Solution(object):
    def isPalindrome(self, s):
        valid=[]
        for ch in s:
            if ch.isalnum():
                valid.append(ch.lower())
            else:
                continue
        n=len(valid)
        left=0
        right=n-1
        while left<right:
            if valid[left]!=valid[right]:
                return False
            left+=1
            right-=1
        return True



            
        

