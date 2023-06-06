class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0
        if len(nums) == k:
            return sum(nums)/k
        
        i = 0
        j = i+k-1
        s = sum(nums[i:j+1])
        maxavg = s/k
        while j< len(nums)-1:
            j +=1
            s = s - nums[i] + nums[j]
            i +=1
            maxavg = max(maxavg, s/k)
            
        return maxavg
        
