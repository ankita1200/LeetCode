class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        if n < 1:
            return 0
        if n == 1:
            return min(matrix[0])
        prev = [matrix[n-1][i] for i in range(n)]
        curr = [0] * n
        
        for row in range(n-2,-1,-1):
            for col in range(n):
                minval = prev[col]
                if col+1<n:
                    minval = min(minval,prev[col+1])
                if col-1>=0:
                    minval = min(minval,prev[col-1])
                curr[col] = matrix[row][col] + minval
            prev = [ele for ele in curr]
                
        return min(curr)
        
        
