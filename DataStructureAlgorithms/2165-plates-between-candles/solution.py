class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        prefix_sum=[0]*(n+1)
        for i,ch in enumerate(s):
            prefix_sum[i+1]=prefix_sum[i]+(ch=="*")
        nearest_left=[0]*n
        nearest_right=[0]*n
        base_left=base_right=-1
        for i,ch in enumerate(s):
            if ch=="|":
                base_left=i
            nearest_left[i]=base_left
        for i in range(n-1,-1,-1):
            if s[i]=="|":
                base_right=i
            nearest_right[i]=base_right
        ans=[0]*len(queries)
        for index,(left,right) in enumerate(queries):
            left_in=nearest_right[left]
            right_in=nearest_left[right]
            if left_in>=0 and right_in>=0 and left_in<right_in:
                ans[index]=prefix_sum[right_in]-prefix_sum[left_in+1]
        return ans
            

            
