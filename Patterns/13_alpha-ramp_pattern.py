#Alpha-Ramp Pattern
n=3
start=ord('A')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=' ')
    start=start+1
    print()

'''
A 
B B 
C C C '''