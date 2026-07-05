#Reverse Letter Triangle Pattern
n=6
for i in range(n,0,-1):
    start=ord('A')
    for j in range(1,i+1):
        print(chr(start),end=' ')
        start=start+1
    print()

'''
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 
'''