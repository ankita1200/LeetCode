class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @cache
        def dp(index,remain):
            if index == len(piles) or remain == 0:
                return 0
            curr = 0
            #skip
            ans = dp(index+1,remain)
            for i in range(min(remain,len(piles[index]))):
                curr = curr+piles[index][i]
                ans = max(ans,curr + dp(index+1,remain-i-1))
            return ans
        
        return dp(0,k)
            

   
        
        
