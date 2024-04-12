class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def helper(pos):
            if dp[pos] != float('inf'):
                return dp[pos]
            for i in range(1,nums[pos]+1):
                next_pos= i + pos
                if next_pos < n:
                    dp[pos] = min(dp[pos],helper(next_pos))
            dp[pos] = 1 + dp[pos]
            return dp[pos]
        
        n=len(nums)
        dp=[float('inf') for _ in range(n)]
        dp[n-1]=0
        helper(0)
        return dp[0]
        

        
