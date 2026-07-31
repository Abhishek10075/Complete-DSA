#Alpha-Triangle Pattern
n=5
first=ord('A')+(n-1)
for i in range(0,n):
    ch=first
    for j in range(0,i+1):
        print(chr(ch),end=' ')
        ch=ch+1
    first=first-1
    print()

'''
E
D E
C D E
B C D E
A B C D E
'''