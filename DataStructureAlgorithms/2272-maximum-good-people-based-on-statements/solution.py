class Solution:        
    def maximumGood(self, statements: List[List[int]]) -> int:
        
        n = len(statements)
        res = 0
        
        def checkGood(person, mask):
            return mask & 1<<person
        
        def validateStatement(mask):
            for i in range(n):
                if checkGood(i, mask):
                    for j in range(n):
                        statement = statements[i][j]
                        
                        if (statement==0 and checkGood(j, mask)) or (statement==1 and not checkGood(j, mask)):
                            return False
            return True
        
        for i in range(1,1<<n): 
            if validateStatement(i):
                res = max(res, bin(i).count('1'))
        return res
