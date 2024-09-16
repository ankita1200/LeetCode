class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        maxarea = 0
        while left < right:
            curr = (right-left)*min(height[left],height[right])
            maxarea = max(maxarea,curr)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return maxarea
            
