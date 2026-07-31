#1. Solution


class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)-1
        arr=sorted(arr)
        lar=arr[n]
        sec_lar=-1
        for i in range(n-1,-1,-1):
            if arr[i]>sec_lar and arr[i] != lar:
                sec_lar=arr[i]
        return sec_lar

'''
TC=o(NlogN)+ o(n)
SC=o(1)
'''
#Solution 2

class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)-1
        lar=-1
        sec=-1
        for i in range(0,n+1):
            if arr[i]>lar:
                sec=lar
                lar=arr[i]
            elif arr[i]>sec and arr[i]!=lar:
                sec=arr[i]
            else:
                continue
        return sec
      
'''
TC=o(N)
SC=o(1)
'''      

## Program to Extract Unique Digits from an Alphanumeric String
s = "dfa9814562321afd"
n=len(s)-1
count=0
digit=set()
for i in range(0,n+1):
    if s[i].isdigit():
        count+=1
        digit.add(int(s[i]))
    else:
        continue
digit_list=list(digit)
print(digit_list)

'''
output
[1, 2, 3, 4, 5, 6, 8, 9]
'''
#find the second largest from the alphnumeric 
class Solution(object):
    def secondHighest(self, s):
        n=len(s)-1
        lar=-1
        sec=-1
        for i in s:
            if i.isdigit():
                if i>lar:
                    sec=lar
                    lar=i
                elif i>sec and i!=lar:
                    sec=i
        return int(sec)
