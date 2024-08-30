class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(index,remain):
            if remain == 0:
                return 1
            if remain < 0 or index>=len(coins):
                return 0
            count = 0
            for i in range(remain//coins[index]+1):
                taken = i*coins[index]
                count += dp(index+1,remain-taken)
            return count

        return dp(0,amount)

        
