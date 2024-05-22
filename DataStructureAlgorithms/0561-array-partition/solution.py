class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        pos=0
        while pos<n:
            val=min(nums[pos],nums[pos+1])
            ans+=val
            pos+=2
        return ans
            
        
