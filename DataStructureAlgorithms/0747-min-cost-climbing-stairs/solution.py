class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        memo[0] = cost[0]
        memo[1] = cost[1]
        n = len(cost)
        for i in range(2, n):
            memo[i] = min(memo[i-1] + cost[i], memo[i-2] + cost[i])
        return min(memo[n-1], memo[n-2])
        
