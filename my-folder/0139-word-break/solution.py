class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dp(i):
            if i<0:
                return True
            for word in wordDict:
                if s[i+1-len(word):i+1] == word and dp(i-len(word)):
                    return True
            return False
        
        return dp(len(s)-1)
        
