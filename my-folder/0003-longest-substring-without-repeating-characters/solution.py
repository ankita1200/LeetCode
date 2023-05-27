class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans= 0
        mp = {}
        left = right = 0
        while right < n:
            r = s[right]
            if r in mp.keys():
                left = max(mp[r] + 1,left) 
            mp[r] = right
            ans = max(ans, right-left + 1)
            right +=1
        return ans

