class Solution:
    def maxArea(self, height: List[int]) -> int:
        l1=0
        n=len(height)
        l2=n-1
        area = 0
        while l1 < l2:
            a = (l2-l1) * min(height[l1], height[l2])
            if height[l1] < height[l2]:
                l1 +=1
            else:
                l2 -=1
            area = max(a,area)

        return area   
