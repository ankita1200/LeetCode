class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @cache
        def dp(index,prev_color,ncount):
            if index == len(houses):
                return 0 if ncount==target else self.maxcost
            if ncount > target:
                return self.maxcost
            
            minpaintcost = self.maxcost
            if houses[index] != 0:
                newcount = ncount + (1 if houses[index]!=prev_color else 0)
                minpaintcost = dp(index+1,houses[index],newcount)
            else:
                total_colors = len(cost[0])
                for color in range(1,total_colors+1):
                    newcount = ncount + (1 if color != prev_color else 0)
                    curr_cost = cost[index][color-1] + dp(index+1,color,newcount)
                    minpaintcost = min(minpaintcost, curr_cost)
            
            return minpaintcost
        
        self.maxcost = 1000001
        ans = dp(0,0,0)
        return ans if ans != self.maxcost else -1
        
        
