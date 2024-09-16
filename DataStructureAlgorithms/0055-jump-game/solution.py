class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        val = [False] * n
        val[n-1] = True
        for i in range(n-2,-1,-1):
           
            end = min(n-1,nums[i]+i)
            for jump in range(end,i,-1):
                if val[jump]:
                    val[i] = True
                    break
            
        return val[0]


        
