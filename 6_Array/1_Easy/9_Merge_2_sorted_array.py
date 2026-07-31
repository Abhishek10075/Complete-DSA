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