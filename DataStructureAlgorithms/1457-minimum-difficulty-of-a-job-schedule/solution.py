class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        n = len(jobDifficulty)
        @cache
        def dp(stindex,remain,day):
            if day == d:
                return max(jobDifficulty[stindex:stindex+remain])
            minval = float('inf')
            maxpick = remain - (d-day)
            for i in range(1,maxpick+1):
                jobs_today = jobDifficulty[stindex:stindex+i]
                minval = min(minval, max(jobs_today)+dp(stindex+i,remain-i,day+1))
            return minval
        ans = dp(0,n,1)
        return ans if ans != float('inf') else -1


        
