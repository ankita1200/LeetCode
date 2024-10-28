class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #subarray 
        # constraint metric - sum of subarray
        # restriction on constraint metric - sum >= target - valid subarray
        # subarr that has minimum length
        #sliding window problem
        left = 0
        currsum = 0
        ans = float('inf')
        for right in range(len(nums)):
            currsum += nums[right]
            if currsum < target:
                continue
            
            while currsum >= target:
                # valid window
                ans = min(ans, right-left+1)
                currsum -= nums[left]
                left += 1
        
        return ans if ans != float('inf') else 0
