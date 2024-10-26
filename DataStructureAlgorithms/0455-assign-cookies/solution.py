class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        gptr = 0
        sptr = 0
    
        while sptr < len(s) and gptr < len(g):
            if s[sptr] >= g[gptr]:
                ans += 1
                gptr += 1
            sptr += 1
                
        return ans
        
