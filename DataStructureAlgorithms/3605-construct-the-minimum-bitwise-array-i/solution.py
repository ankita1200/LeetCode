class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            found = False
            for x in range(nums[i]+1):
                if (x | (x+1)) == nums[i]:
                    ans.append(x)
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
        
