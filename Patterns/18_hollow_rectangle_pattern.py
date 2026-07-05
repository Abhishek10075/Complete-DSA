n=5
for i in range(1,n+1):
            if i==1 or i==n:
                for j in range(1,n+1):
                    print('*',end='')
            else:
                for j in range(1,2):
                    print('*'+' '*(n-2)+'*',end='')
            print(' ')
print('Method 2')
#method 2
for i in range(1,n+1):
    for j in range(1,n+1):
          if i==1 or i==n or j==1 or j==n:
              print('*',end='')
          else:
            print(' ',end='')
    print()
    
'''
*****
*   *
*   *
*   *
*****
'''