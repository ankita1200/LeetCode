class Solution:
    def getFactors(self, n):
        if n == 1: return []

        def backtrack(n,idx,path):
            if path:
                res.append(path + [n])

            for i in range(idx,int(math.sqrt(n))+1):
                if n%i == 0:
                    backtrack(n//i,i,path+[i])

        res = []
        backtrack(n,2,[])
        return res
