class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        print(left_max)
        left_max[0]=height[0]
        right_max[n-1]=height[n-1]
        for i in range(1,n):
            left_max[i]=max(left_max[i-1],height[i])
        for i in range(n-2,-1,-1):
            right_max[i]=max(right_max[i+1],height[i])
        ans=0
        for i in range(n):
            ans+=min(right_max[i],left_max[i])-height[i]
        return ans
        
