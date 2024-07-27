class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        B = [i for i in range(1, len(nums)) if nums[i]%2==nums[i-1]%2]
        ans=[]
        
        for q in queries:
            
            L = bisect_right(B, q[0])
            
            R = bisect_right(B, q[1])
        
            if R-L==0:
                ans.append(True)
            else:
                ans.append(False)
            
        return ans
