class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @cache
        def dp(day,holding,remain):
            if day == len(prices) or remain==0:
                return 0
            buy= sell = 0
            if holding:
                sell = prices[day] + dp(day+1,False,remain-1)
            else:
                buy = -prices[day] + dp(day+1,True,remain)
            skip = dp(day+1,holding,remain)
            return max(skip,buy,sell)
        
        return dp(0,False,k)
        
