class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def makeCombination(s):
            c1 = s.count("(")
            c2 = s.count(")")
            if c1 > n or c2 > n:
                return
            if c2 > c1:
                return
            if len(s) == 2*n and c1 == c2:
                ans.append("".join(s))
                return
            s.append("(")
            makeCombination(s)
            s.pop()
            s.append(")")
            makeCombination(s)
            s.pop()
            return 
        
        ans = []
        makeCombination([])
        return ans
        
