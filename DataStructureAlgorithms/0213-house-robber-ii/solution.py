class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        f = {}
        n = len(nums) -1
        f[n-1] = nums[-2]
        f[n-2] = max(nums[-2], nums[-3])
        for i in range(n-3,-1,-1):
            f[i] = max(nums[i]+f[i+2], f[i+1])
        a=f[0]
        f = {}
        f[n] = nums[-1]
        f[n-1] = max(nums[-1], nums[-2])
        for i in range(n-2,0,-1):
            f[i] = max(nums[i]+f[i+2], f[i+1])
        b = f[1]
        return max(a,b)
