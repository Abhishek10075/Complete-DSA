class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        ele=[]
        for i in range(0,n):
            count=0
            for j in range(i,n):
                if nums[i]==nums[j]:
                    count+=1
            if count>n//3:
               if nums[i] not in ele:
                ele.append(nums[i])
        return ele


'''
TC=o(n*n)+o(n log n)
SC=o(1)
'''

