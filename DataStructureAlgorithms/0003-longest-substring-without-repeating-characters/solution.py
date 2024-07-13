class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        check = set()
        maxlen=0
        left=right=0
        while right<len(s):
            if s[right] not in check:
                check.add(s[right])
            else:
                while s[left]!=s[right]:
                    check.remove(s[left])
                    left+=1
                left+=1
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen
        
