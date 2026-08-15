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

#Optimal solution
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)

        count1, count2 = 0, 0
        ele1, ele2 = 0, 0

        # Find candidates
        for i in range(n):
            if count1 == 0 and nums[i] != ele2:
                ele1 = nums[i]
                count1 = 1

            elif count2 == 0 and nums[i] != ele1:
                ele2 = nums[i]
                count2 = 1

            elif nums[i] == ele1:
                count1 += 1

            elif nums[i] == ele2:
                count2 += 1

            else:
                count1 -= 1
                count2 -= 1

        # Verify candidates
        c1, c2 = 0, 0

        for i in range(n):
            if nums[i] == ele1:
                c1 += 1

            elif nums[i] == ele2:
                c2 += 1

        # Return valid majority elements
        result = []

        if c1 > n // 3:
            result.append(ele1)

        if c2 > n // 3:
            result.append(ele2)

        return result
    '''
    TC=o(n)
    SC=o(1)
    '''