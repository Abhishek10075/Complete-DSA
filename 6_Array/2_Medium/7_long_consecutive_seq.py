#Solution 1->Brute
class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)-1
        m=0
        n=len(nums)-1
    
        for i in range(0,n+1):
            num=nums[i]
            count=1
            while num+1 in nums:
                count+=1
                num+=1
            m=max(m,count)
        return m


'''
TC=o(n*n)
sc=o(1)
'''

#Solution 2->Better
class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        n=len(nums)-1
        count=0
        last_smaller=float('-inf')
        longest=0
        for i in range(0,n+1):

            #nums =[0,1,1,2]
            if i==0:
                count=1
                last_smaller=nums[0]
            if nums[i] == last_smaller:
                continue
            elif nums[i] - 1 == last_smaller:
                count += 1
                last_smaller = nums[i]
            else:
                longest=max(longest,count)
                count = 1
                last_smaller = nums[i]
        longest=max(longest,count)
        return longest


'''
TC=n log(n) + o(n)
SC=o(1)
'''