n=1221
num_copy=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reverse of number:",rev)
if rev==num_copy:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
'''

TC=O(log₁₀ n)
SC=O(1)
o/p->Number is palindrome
'''