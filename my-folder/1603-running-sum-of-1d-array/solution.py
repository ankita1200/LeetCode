class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        ans=[nums[0]]
        for i in range(1,len(nums)):
            ans.append(ans[i-1]+nums[i])
        return ans
        
