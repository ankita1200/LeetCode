class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dp(index,remainzero, remainone):
            if index == len(strs):
                return 0
            #count 0s and 1s
            countzero = strs[index].count('0')
            countone = strs[index].count('1')
            #skip this index
            pathcount1 = dp(index+1,remainzero,remainone)
            pathcount2 = 0
            if countzero <= remainzero and countone<=remainone:
                pathcount2 = 1 + dp(index+1,remainzero-countzero,remainone-countone)
            return max(pathcount1,pathcount2)
        
        return dp(0,m,n)
        
