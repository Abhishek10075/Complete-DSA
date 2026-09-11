#Solution 1 ->Brute
class Solution(object):
    def longestConsecutive(self, nums):
        n=len(nums)-1
        maxi=0
        for i in nums:#o(n)
            count=1
            num=i
            while num+1 in nums:#o(n)
                count+=1
                num=num+1
            maxi=max(count,maxi)
        return maxi
'''
TC=o(n*n)
SC=o(1)
'''

#Better using sorting method
class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        n=len(nums)-1
        last_smaller=float('-inf')
        longest=0
        count=0
        for i in range(0,n+1):
            if count==0:
                last_smaller=nums[i]
                count=1
            if nums[i]==nums[i-1]+1:
                count+=1
                longest=max(longest,count)
            elif nums[i]==nums[i-1]:
                longest=max(longest,count)
                continue
            elif nums[i]!=nums[i-1]:
                last_smaller=nums[i]
                count=1
            longest=max(longest,count)
        return longest
            

#better correct version
class Solution(object):
    def longestConsecutive(self, nums):

        nums.sort()

        n = len(nums) - 1
        last_smaller = float('-inf')
        longest = 0
        count = 0

        for i in range(0, n + 1):
            num = nums[i]

            if num - 1 == last_smaller:
                count += 1
                last_smaller = num

            elif num != last_smaller:
                count = 1
                last_smaller = num

            longest = max(longest, count)

        return longest

#optimal solution using set
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        longest=0
        count=1
        my_set=set()
        for num in nums:
            my_set.add(num)
        n=len(my_set)-1
        for i in my_set:
            num=i
            if num-1 not in my_set:
                count=1
                x=num
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(longest,count)
    
        return longest