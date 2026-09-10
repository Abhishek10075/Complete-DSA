class Solution:
    def findUnion(self, a, b):
        n1 = len(a)
        n2 = len(b)

        i, j = 0, 0
        result = []

        while i < n1 and j < n2:
            if a[i] <= b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
            else:
                if not result or result[-1] != b[j]:
                    result.append(b[j])
                j += 1

        while i < n1:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1

        while j < n2:
            if not result or result[-1] != b[j]:
                result.append(b[j])
            j += 1

        return result
'''
TC=TC(n+m)
SC=SC(n+m)
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        result = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < m:
            result.append(nums1[i])
            i += 1

        while j < n:
            result.append(nums2[j])
            j += 1

        # Copy result back into nums1
        for k in range(m + n):
            nums1[k] = result[k]



    #optimal solution
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=m-1
        j=n-1
        k=m+n-1

        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while j>=0: #may be nums2 has some elements left ,nums1 has all elements in place
            nums1[k]=nums2[j]
            j-=1
            k-=1

        return nums1