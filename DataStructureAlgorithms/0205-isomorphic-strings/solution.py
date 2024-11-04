class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        exists = set()
        for s_x,t_x in zip(s,t):
            if (s_x in mapping and mapping[s_x]!=t_x) or (not s_x in mapping and t_x in exists):
                return False
            mapping[s_x] = t_x
            exists.add(t_x)
            
        return True
