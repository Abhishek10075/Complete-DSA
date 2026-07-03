 #Binary Number Triangle Pattern
n=6
start=1
for i in range(0,n):
    if i%2==0:
        start=1
    else:
        start=0
    
    for j in range(0,i+1):
        print(start,end=' ')
        if start==0:
           start=start+1
        else:
           start=start-1
    print()

'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
'''