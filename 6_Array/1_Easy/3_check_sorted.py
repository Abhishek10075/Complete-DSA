#Check array sorted or not
class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        n=len(arr)-1
        if n==0:
            return True
        for i in range(1,n+1):
            if arr[i]>=arr[i-1]:
                continue
            else:
                return False
        return True


 #count break point
'''

Input: [1,2,3,4] Output: 0
Input: [3,4,5,1,2] Output: 1
Input: [2,1,3,4]  Output: 1
Input: [4,1,3,2] Output: 2
'''
arr=[4,1,3,2]
n=len(arr)-1
count=0
for i in range(0,n):
    if arr[i+1]>arr[i]:
        continue
    else:
        count+=1
print(count)

#find break point
'''
Input: [4,5,1,2,3] Output: 2
Input: [1,2,3,4] Output: 0
Input: [6,7,8,1,2,3,4] Output: 3
'''
arr=[6,7,8,1,2,3,4]
n=len(arr)-1
break_point=0
for i in range(0,n):
    if arr[i]>arr[i+1]:
        break_point=i+1
        break
    elif arr[i]>arr[i+1]:
        continue
print(break_point)

#check array sorted and roated
class Solution:
    def check(self, nums):
        n = len(nums)
        break_count = 0

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                break_count += 1

        if nums[-1] > nums[0]:
            break_count += 1

        if break_count <= 1:
            return True
        else:
            return False