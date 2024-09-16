class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        maxlen = 0
        seen = set()
        while right < len(s):
            if not s[right] in seen:
                seen.add(s[right])
            else:
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        break
                    else:
                        seen.remove(s[left])
                    left += 1
            right += 1
            maxlen=max(maxlen,right-left)
        return maxlen
                
                
            
        
