def countDigit(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
n=12345
print(countDigit(123))

'''
TC=O(log10n)
SC=O(1)
o/p->3
'''