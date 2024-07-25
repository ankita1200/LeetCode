class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=maxsub=nums[0]
        for num in nums[1:]:
            curr=max(num,curr+num)
            maxsub=max(curr,maxsub)
        return maxsub
        
