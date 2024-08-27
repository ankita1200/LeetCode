class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @cache
        def dp(index,stock):
            if index >= len(prices):
                return 0
            if stock:
                #sell or skip
                return max((-fee + prices[index] + dp(index+1,False)), dp(index+1,True))
            else:
                return max((-prices[index] + dp(index+1,True)), dp(index+1,stock))
        
        return dp(0,False)
                           
                
        
