class Solution:
    def rob(self, nums: List[int]) -> int:
        f = {}
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        n = len(nums) -1
        f[n] = nums[-1]
        f[n-1] = max(nums[-1], nums[-2])
        for i in range(n-2,-1,-1):
            f[i] = max(nums[i]+f[i+2], f[i+1])
        return f[0]
