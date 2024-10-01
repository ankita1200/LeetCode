class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        @lru_cache
        def dp(index,color):
            if index == len(costs):
                return 0
            return costs[index][color] + min(dp(index+1,(color+1)%3), dp(index+1,(color+2)%3))
        
        return min(dp(0,0),dp(0,1),dp(0,2))
        
