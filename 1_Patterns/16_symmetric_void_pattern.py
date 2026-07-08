n=5
# Upper Half
for i in range(n, 0, -1):

    # Left stars
    for j in range(i):
        print('*', end='')

    # Middle spaces
    for k in range(2 * (n - i)):
        print(' ', end='')

    # Right stars
    for j in range(i):
        print('*', end='')

    print()

# Lower Half
for i in range(n):

    # Left stars
    for j in range(i + 1):
        print('*', end='')

    # Middle spaces
    for k in range(2 * (n - i - 1)):
        print(' ', end='')

    # Right stars
    for j in range(i + 1):
        print('*', end='')

    print()

'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''