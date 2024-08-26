class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(currsum):
            if currsum == 0:
                return 0
            if currsum < 0:
                return float('inf')
            mincount = float('inf')
            for coin in coins:
                mincount = min(mincount,dp(currsum-coin))
            return 1 + mincount
        
        val = dp(amount)
        return val if val != float('inf') else -1
        
