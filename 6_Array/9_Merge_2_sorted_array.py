arr1=[1,1,2,3,4]
arr2=[1,5,6]
n1=len(arr1)-1
n2=len(arr2)-1
i,j=0,0
result=[]
while i<n1+1 and j<n2+1:
    if arr1[i]<=arr2[j]:
        if len(result)==0 or result[-1]!=arr1[i]:
            result.append(arr1[i])
        i+=1
    else:
        if len(result)==0 or result[-1]!=arr2[j]:
            result.append(arr2[j])
        j+=1
while i<n1+1:
    if len(result)==0 or result[-1]!=arr1[i]:
        result.append(arr1[i])
    i+=1
while j<n2+1:
    if len(result)==0 or result[-1]!=arr2[j]:
        result.append(arr2[j])
        j+=1

print("tow array merge in sorted order:",result)

for i in range(0,n1+1):
    arr1[i]=result[i]
    last_index=i
print(i)
result_size=len(result)-1
k=0
for i in range(i+1,result_size+1):
    arr2[k]=result[i]
    k+=1
arr2=arr2[:k]

print(result)
print(arr1)
print(arr2)

#find intersection for two sorted array

