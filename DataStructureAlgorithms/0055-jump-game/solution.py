class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @cache
        def dp(index):
            if index >= len(nums)-1:
                return True
            for i in range(1,nums[index]+1):
                if dp(index+i):
                    return True
            return False
        
        return dp(0)
        
