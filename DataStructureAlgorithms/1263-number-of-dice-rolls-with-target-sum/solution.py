class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def dp(index,remain):
            if index==0:
                return 1 if remain==0 else 0
            if remain < 0:
                return 0
            count = 0
            for face in range(1,k+1):
                count += dp(index-1,remain-face)
            return count

        return dp(n,target) % (10**9 + 7)

        
