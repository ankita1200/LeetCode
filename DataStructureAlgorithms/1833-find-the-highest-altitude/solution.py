class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        ans = 0
        for i in range(len(gain)):
            prefix_sum += gain[i]
            ans = max(ans,prefix_sum)
        return ans 
        
