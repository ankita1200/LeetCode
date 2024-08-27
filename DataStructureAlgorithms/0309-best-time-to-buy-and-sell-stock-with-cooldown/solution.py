class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dp(day,holding,cooldown):
            if day == len(prices):
                return 0
            # skip
            ans = dp(day+1,holding,False)
            if holding:
                ans = max(ans, prices[day]+dp(day+1,False,True))
            elif not cooldown:
                ans = max(ans, -prices[day]+dp(day+1,True,False))
            return ans
        
        return dp(0,False,False)
                
        
