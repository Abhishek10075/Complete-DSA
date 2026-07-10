#Solution 1->Brute 

'''
class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        for i in range(0,k):#o(r)
            last_el=nums.pop()#o(1)
            nums.insert(0,last_el)#o(N)


  TC=o(r*N)
  SC=O(1)
'''
        
        
#Solution 2 
'''
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)

        k = k % n  # Important step

        nums[:] = nums[n-k:] + nums[:n-k]

TC=o(k)+o(n-k)
SC=o(1)
'''

#solution 3->optimal solution
'''

def reverse(nums,left,right):
    n=len(nums)
    while left<=right:
        nums[left], nums[right]=nums[right],nums[left]
        left+=1
        right-=1
reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)
'''