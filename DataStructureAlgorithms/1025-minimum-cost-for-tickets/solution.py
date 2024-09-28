class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(index,remain):
            if index == len(days)-1:
                return 0 if remain > 0 else mincosts
            ndays = days[index+1] - days[index]
            if remain > 0:
                return dp(index+1,max(0,remain-ndays))
            
            return min(costs[0] + dp(index+1,0),costs[1] + dp(index+1,max(0,7-ndays)),costs[2] + dp(index+1,max(0,30-ndays)))

        mincosts = min(costs)    
        return dp(0,0)
            
        
