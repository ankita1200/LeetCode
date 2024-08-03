class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def minCoins(amt):
            if amt<0:
                return -1
            if amt==0:
                return 0
            minNo=float('inf')
            for coin in coins:
                val = minCoins(amt-coin)
                if val>=0:
                    minNo = min(minNo, val)
            if minNo==float('inf'):
                return -1
            else:
                return 1+ minNo

        return minCoins(amount)
