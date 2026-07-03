#Reverse Letter Triangle Pattern
n=6
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()

'''
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 
'''