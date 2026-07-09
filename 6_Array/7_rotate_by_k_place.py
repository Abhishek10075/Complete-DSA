class Solution(object):
    def rotate(self, nums, k):
        for i in range(0,k):
            last_el=nums.pop()
            nums.insert(0,last_el)
        
        return nums
        
        