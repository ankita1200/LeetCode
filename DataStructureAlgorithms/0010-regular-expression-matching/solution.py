class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        spl = set(['.','*'])
        @cache
        def matchAt(i,j):
            if i==len(s) and j==len(p):
                return True
            if j==len(p):
                return i==len(s)
            curr_match = (i< len(s)) and (s[i]==p[j] or p[j]=='.')
            # case when next character is a *
            if j+1 < len(p) and p[j+1]=='*':
                # skip the curr charater at p if there is a mismatch. Else is there is a match then just call by shifting i
                return matchAt(i,j+2) or (curr_match and matchAt(i+1,j))
            else:
                return curr_match and matchAt(i+1,j+1)
        
        return matchAt(0,0)
