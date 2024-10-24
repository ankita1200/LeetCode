class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = len(word1)
        y = len(word2)
        l = min(x,y)
        ans = ""
        for letter1,letter2 in zip(word1[:l],word2[:l]):
            ans += letter1 + letter2
        ans += word1[l:] if l<x else word2[l:]
        return ans

