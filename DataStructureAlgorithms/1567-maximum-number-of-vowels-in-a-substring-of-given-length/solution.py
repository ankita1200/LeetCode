class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])
        left = 0
        countvowel = 0
        ans = 0
        for right in range(len(s)):
            if s[right] in vowels:
                countvowel += 1
            if right-left+1 == k:
                ans = max(ans,countvowel)
                if s[left] in vowels:
                    countvowel -= 1
                left += 1
        return ans


        
