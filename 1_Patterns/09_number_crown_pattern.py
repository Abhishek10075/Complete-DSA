# Number Crown Pattern
n=6
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(1,(2*n-2*i)+1):
        print(' ',end=' ')
    for l in range(i,0,-1):
        print(l,end=' ')
    print()
'''
1      1
12    21
123  321
12344321
'''