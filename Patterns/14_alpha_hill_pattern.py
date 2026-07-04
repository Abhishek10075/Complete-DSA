

#Alpha Hill Pattern
N=4
for i in range(N):

        # Print leading spaces
        print(" " * (N - i - 1), end="")

        # Initialize character to start from 'A'
        ch = ord('A')
        breakpoint = (2 * i + 1) // 2

        # Print characters in row
        for j in range(1, 2 * i + 2):
            print(chr(ch), end="")
            if j <= breakpoint:
                ch += 1
            else:
                ch -= 1

         # Print leading spaces->optional because we are not printing anything after the characters space 
         #will be printed automatically in the next line but if you want to print it explicitly then you
         #  can use the below code 
        
        print(" " * (N - i - 1), end="")
        print()

'''  
   A
  ABA
 ABCBA
ABCDCBA
'''