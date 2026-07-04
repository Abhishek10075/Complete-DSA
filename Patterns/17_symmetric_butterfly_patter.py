#Symmetric Butterfly Pattern

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    for k in range(1,(2*(n-i))+1):
        print(' ',end='')
    for l in range(1,i+1):
        print('*',end='')
    print()
    
for m in range(n-1,0,-1):
    for q in range(1,m+1):
        print('*',end='')
    for o in range(1,(2*(n-m))+1):
        print(' ',end='')
    for p in range(1,m+1):
        print('*',end='')
    print()

    