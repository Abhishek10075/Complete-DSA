#print 4 Time Abhiishe
print("Print Name 4 time using Recursion.")
count=1
def name():
    global count
    if count==5:
        return
    print("Abhishek")
    count+=1
    name()
name()


#Print N to 1
print("Print 1 to N using Recursion ")
N=int(input("Enter the N:"))
i=1
def count(i,N):
    if i==N:
        return
    print(i)
    i+=1
    count(i,N)
count(i,N)


#print linearly N to 1
N=int(input("Enter the N:"))
def count(N):
    if N==0:
        return
    print(N)
    count(N-1)
count(N)


#print N to 1 using Backtracking
N=int(input("Enter the N:"))
i=1
def count(i,N):
    if i==N:
        return
    count(i+1,N)
    print(i)
count(i,N)
    
    
#print 1 to to using Backtracking
N=int(input("Enter the N:"))
def fun(N):
    if N==0:
        return
    fun(N-1)
    print(N)
fun(N)
    
    