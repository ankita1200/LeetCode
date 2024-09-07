class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        L = [0] * n
        R = [0] * n
        L[0] = 1
        R[n-1] = 1
        for i in range(1,n):
            L[i] = nums[i-1] * L[i-1]
        
        for i in range(n-2,-1,-1):
            R[i] = nums[i+1] * R[i+1]
        
        ans = [0] * n
        for i in range(n):
            ans[i] = L[i]*R[i]
        
        return ans
        
