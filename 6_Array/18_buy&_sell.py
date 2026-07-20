#Solution 1->Brute
class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)-1
        max_prof=0
        for i in range(0,n+1):
            for j in range(i+1,n+1):
                if prices[j]>prices[i]:
                    max_prof=max(max_prof,prices[j]-prices[i])
        return max_prof
        
'''
TC=o(n*n)
SC=o(1)
'''
#Solution 2->optimal 
class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)-1
        max_prof=0
        min_price=float('inf')
        for i in range(0,n+1):
            if prices[i]< min_price:
                min_price=prices[i]
            if prices[i]>min_price:
                profit=prices[i]- min_price
                max_prof=max(max_prof,profit)
        return max_prof
'''
TC=o(n)
SC=o(1)
'''