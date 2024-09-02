class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        count1 = count0 = 0
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
            if nums[i] == 0:
                count0 += 1
            else:
                count1 += 1
        
        @cache
        def dp(index,odd):
            if index >= len(nums):
                return 0
            if nums[index] % 2 == odd:
                return 1 + dp(index+1,1-odd)
            else:
                return dp(index+1,odd)
        
        return max(count0,count1,dp(0,0),dp(0,1))
        
            
            

        
