#Increasing Letter Triangle Patter
n=6
for i in range(1,n+1):
    start=ord('A')
    for j in range(1,i+1):
        print(chr(start),end=' ')
        start=start+1
    print()
'''
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F
'''