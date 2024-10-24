class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]+nums[i]
        
        for i in range(len(nums)):
            left_sum = prefix[i]-nums[i]
            right_sum = tot - prefix[i]
            if left_sum==right_sum:
                return i
        return -1
        
