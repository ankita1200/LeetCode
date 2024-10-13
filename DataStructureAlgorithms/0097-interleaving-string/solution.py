class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s3) < len(s1)+len(s2):
            return False
        
        @cache
        def dp(index1,index2,index3):
            if index3 == len(s3) and index1==len(s1) and index2==len(s2):
                return True
            if index3 == len(s3):
                return False
            
            if (index1 < len(s1)) and (s1[index1] == s3[index3]) and dp(index1+1,index2,index3+1):
                    return True
            if (index2 < len(s2)) and (s2[index2] == s3[index3]) and dp(index1,index2+1,index3+1):
                    return True
            return False
            
        return dp(0,0,0)

        
