class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minVal = {}
        minVal[0] = minVal[1]=0
        n = len(cost)
        for i in range(2,n+1):
            minVal[i]=min(minVal[i-2]+cost[i-2],minVal[i-1]+cost[i-1])
        return minVal[n]
