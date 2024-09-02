class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell atmost 2 times. buy atmost 2 times
        
        @cache
        def dp(index,holding,k):
            if index == len(prices) or k==0:
                return 0
            maxval = dp(index+1,holding,k)
            if holding:
                return max(prices[index]+dp(index+1,False,k-1),maxval)
            else:
                return max(-prices[index]+dp(index+1,True,k),maxval)
        
        return dp(0,False,2)
        
