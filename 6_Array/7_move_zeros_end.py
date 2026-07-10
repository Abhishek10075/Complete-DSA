#Solution 1
'''
arr=[1,0,2,3,2,0,0,4,5,1]
n=len(arr)-1
temp=[]
for j in range(0,n+1):#o(n)
    if arr[j]!=0:
        temp.append(arr[j])

i=0
n2=len(temp)-1
print(n2)
for j in range(0,n2+1):#o(n2)
    arr[i]=temp[j] 
    i+=1

for j in range(n2+1,n+1):#o(n1-n2)
    arr[j]=0
print(temp)
print(arr)

TC=o(n)+ o(n2)+oN(n1-n2)
SC=o(n2)->o(n)
'''

#Solution 2 ->optimal
arr=[1,0,2,3,2,0,0,4,5,1]

n=len(arr)-1
for j in range(0,n+1):
    if arr[j]!=0:
        i=j
    elif arr[j]==0:
        
