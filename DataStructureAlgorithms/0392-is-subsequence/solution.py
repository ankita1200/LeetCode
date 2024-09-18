class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        count = 0
        while j < len(t) and i < len(s):
            if s[i]==t[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        if count == len(s):
            return True
        return False

        
