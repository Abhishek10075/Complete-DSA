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

#Better using dictionary
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        frequence={}
        major_ele=[]
        for i in range(0,n):
            if nums[i] not in frequence:
                frequence[nums[i]]=1
            else:
                 frequence[nums[i]]+=1
        for k,v in frequence.items():
            if v>n//3:
                major_ele.append(k)
        return major_ele
                
'''
TC=o(n)+o(n)~o(n)
SC=O(n)
'''