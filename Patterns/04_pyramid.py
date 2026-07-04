
n=5
for i in range(0,n):
    print(' '*(n-i-1) + '*'*(i*2+1)+' '*(n-i-1))
print()

'''
     *
    ***
   *****
  *******
 *********
'''

#Method 2

n=4
for i in range(0,n):
    for j in range(0,(n-i-1)):
        print(' ',end='')
    for k in range(0,(2*i+1)):
        print('*',end='')
    for l in range(0,(n-i-1)):
        print(' ',end='')
    print()
