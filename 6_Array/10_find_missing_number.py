#Solution 1
'''
num=[8, 2, 4, 5, 3, 7, 1]
n=len(num)
print("Len:",n)
for i in range(0,n+1):#o(N)
    if i not in num: #o(N)
        print(i)
TC=o(N*N)
SC=o(1)
'''

#Solution 2
'''
nums=[9,6,4,2,3,5,7,0,1]
n=len(nums)-1
freq={}
for i in range(0,n+1):
    freq[i]=0
print(freq)

for num in nums:
    freq[num]=1
print(freq)

for k,v in freq.items():
    if v==0:
        print('Missing Number',k)

TC=o(N)+o(N)+o(N)
SC=o(N)
'''


#Solution 3
'''
num=[8, 2, 4, 5, 3, 7, 1]
n=len(num)
print('Size of num',n)
num_sum=0
for i in range(0,n):
    print(num[i])
    num_sum=num_sum+num[i]
    last_index=i
print("Sum of array numbers:",num_sum)
natural_sum=0
print("Last index",last_index)
for i in range(1,last_index+3):
    print(i)
    natural_sum=natural_sum+i
print("Sum of natural number:",natural_sum)
missing_number=natural_sum-num_sum
print("Missing number is ",missing_number)
'''

#Solution 4->optimal
nums=[8, 2, 4, 5, 3, 7, 1,6,10]
#Sum of natural number (n(n+1)/2)
n=len(nums)
n=n+1#we have to add the one extra to find the last number 
sum_natural=(n*(n+1))//2#TC=O(N)
sum_num=sum(nums)#TC=O(N)
missing_num=sum_natural-sum_num
print("Missing number :",missing_num)

'''
TC=O(N)+O(N)
SC=O(1)
'''