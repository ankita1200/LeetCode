class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(index,holding):
            if index == len(prices):
                return 0
            #skip
            val = dp(index+1,holding)
            if holding:
                #skip or sell
                return max(val,prices[index]+dp(index+1,not holding))
            else:
                return max(val,-prices[index]+dp(index+1,not holding))
        return dp(0,False)   
