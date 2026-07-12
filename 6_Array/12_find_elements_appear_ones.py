#Solution 1-Brute 

class Solution:
    def findUnique(self, arr):
        # code here 
        n=len(arr)-1
        for i in range(0,n+1):
            count=0
            for j in range(0,n+1):
                if arr[j]==arr[i]:
                    count+=1
            if count==1:
                return arr[i]
'''
TC=o(N*N)
SC=o(1)
'''

#Solution 2 -Better usign hashing

class Solution:
    def findUnique(self, arr):
        hash_map = {}

        # Count frequency
        for num in arr:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        # Find unique element
        for num in arr:
            if hash_map[num] == 1:
                return num
'''
TC=o(2N)
SC=o(N)
'''

#optimal solution
class Solution:
    def findUnique(self, arr):
        ans = 0

        for num in arr:
            ans ^= num

        return ans
'''
TC=o(n)
SC=o(1)
'''