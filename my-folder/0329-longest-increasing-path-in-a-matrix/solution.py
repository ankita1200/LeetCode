class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        dp=[[1]*cols for _ in range(rows)]
        visited=set()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if (r,c) in visited:
                return dp[r][c]
            visited.add((r,c))
            maxpath=0
            for dr,dc in directions:
                newr,newc=r+dr,c+dc
                if newr<0 or newc<0 or newr==rows or newc==cols or matrix[newr][newc]<=matrix[r][c]:
                    continue
                maxpath=max(maxpath,dfs(newr,newc))
            dp[r][c]=1+maxpath
            return dp[r][c]

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited:
                    dfs(i,j)
        return max(map(max,dp))
        
