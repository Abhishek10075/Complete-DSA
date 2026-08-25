#81. Search in Rotated Sorted Array II->optimal Solution->solved by My self
class Solution(object):
    def search(self, nums, target):
        n=len(nums)-1
        l=0
        r=n
        if n==0:
            if nums[0]==target:
                return True
            elif nums[0]!=target:
                return False
        

        while l<=r:
            if nums[l]==target or nums[r]==target:
                return True
            mid=(l+r)//2
           
            if  nums[mid]==target:
                return True
            elif nums[mid]==nums[l]==nums[r]:
                l+=1
                r+=-1
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<=nums[r]:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False

#Taking the reference for better solution and slight modification in my solution
class Solution(object):
    def search(self, nums, target):
        n=len(nums)-1
        l=0
        r=n
        while l<=r:
            if nums[l]==target or nums[r]==target:
                return True
            mid=(l+r)//2
           
            if  nums[mid]==target:
                return True
            elif nums[mid]==nums[l]==nums[r]:
                l+=1
                r+=-1
                continue
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<=nums[r]:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False

        
             
        