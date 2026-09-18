class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        s_sort=sorted(s)
        t_sort=sorted(t)
        if s_sort==t_sort:
            return True
        
        return False

'''
TC=O(nlogn)+O(nlogn)
SC=O(n)+O(n)
'''  

#Optimal Solution
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False

        f={}
        for i in range(0,len(s)):
            if s[i] not in f:
                f[s[i]]=1
            elif s[i] in f:
                f[s[i]]+=1
        
        for j in range(0,len(t)):
            if t[j] not in f:
                return False
                break
            elif t[j] in f:
                f[t[j]]-=1
            
            if f[t[j]]<0:
                return False
                break
        return True
'''
TC=O(n)+O(n)
SC=o(26)=o(1)
'''