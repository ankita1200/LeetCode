class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        currcost = 0
        ans = 0
        for right in range(len(s)):
            if s[right]!=t[right]:
                currcost += abs(ord(s[right])-ord(t[right]))
            
            while (currcost > maxCost) and left<=right:
                if s[left] != t[left]:
                    currcost -= abs(ord(s[left])-ord(t[left]))
                left += 1
            
            ans = max(ans,right-left+1)

        return ans    



