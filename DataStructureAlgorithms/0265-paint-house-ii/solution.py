class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        @lru_cache
        def dp(index,prev_color_index):
            if index >= len(costs):
                return 0
            mincost = float('inf')
            for color_index,color in enumerate(costs[index]):
                if color_index != prev_color_index:
                    mincost = min(mincost,color + dp(index+1,color_index))
            return mincost
        
        return dp(0,-1)
                    
        
