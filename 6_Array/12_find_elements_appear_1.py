#Solution 1-Brute 
'''
arr=[1,1,2,3,3,4,4]
for i in range(0,len(arr)):
    num=arr[i]
    c=0
    for j in range(0,len(arr)):
        if arr[j]==num:
            c+=1
    if c==1:
        print(num)
    
TC=o(N*N)
SC=o(1)
'''

#Solution 2 -Better usign hashing
'''
arr=[1,1,2,3,3,4,4]
n=len(arr)-1
hash_map={}
print('Size of array',n)
maxi=float('-inf')
for i in range(0,n+1):
    maxi=max(arr[i],maxi)
print('Max element in array',maxi)

for i  in range(0,maxi+1):
    hash_map[i]=0

for i in range(0,n+1):
    count=0
    if arr[i] not in hash_map:
        hash_map[arr[i]]=1
    elif arr[i] in hash_map:
        hash_map[arr[i]]+=1
print("element with count",hash_map)

for i in range(0,n+1):
    if hash_map[arr[i]]==1:
        print('This element appear one time:',arr[i])

TC=o(4N)
SC=o(N)
'''