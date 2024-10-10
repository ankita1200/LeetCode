class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        map = defaultdict(int)
        substr = s[0:10]
        map[substr] += 1
        right = 10
        while right < len(s):
            substr = substr[1:] + s[right]
            map[substr] += 1
            right += 1
        ans = [key for key,count in map.items() if count>1]
        return ans

        
