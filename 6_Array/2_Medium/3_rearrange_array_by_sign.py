#Solution 1-Brute
class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        pos_elm=[]
        neg_elm=[]
        for i in range(n):
            if nums[i]>0:
                pos_elm.append(nums[i])
            if nums[i]<0:
                neg_elm.append(nums[i])
        
        pos_ind=0
        for j in range(len(pos_elm)):
            nums[pos_ind]=pos_elm[j]
            pos_ind+=2
        neg_ind=1
        for k in range(len(neg_elm)):
            nums[neg_ind]=neg_elm[k]
            neg_ind+=2
        return nums


'''
TC=O(n)+O(n/2)+O(n/2)=O(2n)=O(n)
SC=O(n/2)+O(n/2)=O(n)
'''

#Solution 2-Optimal
class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        pos_ind=0
        neg_ind=1
        result=[0]*n
        for i in range(n):
            if nums[i]>0:
                result[pos_ind]=nums[i]
                pos_ind+=2
            elif nums[i]<0:
                result[neg_ind]=nums[i]
                neg_ind+=2
        return result

'''
TC=o(n)
SC=o(n)
'''