class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i = j =0
        substr =""
        maxlen = 0
        while j< len(s):
            substr += s[j]
            while len(Counter(substr)) > 2:
                i +=1
                substr = s[i:j+1]
            maxlen = max(maxlen, len(substr))
            j +=1
        return maxlen
                    
        
