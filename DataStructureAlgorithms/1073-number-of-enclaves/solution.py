class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def dfs(row,col):
            grid[row][col]=0
            for dx,dy in dirs:
                nrow,ncol = row+dx, col+dy
                if 0<=nrow<m and 0<=ncol<n and grid[nrow][ncol]==1:
                    dfs(nrow,ncol)
        
        for j in range(n):
            if grid[0][j]==1:
                dfs(0,j)
            if grid[m-1][j]==1:
                dfs(m-1,j)
        
        for i in range(1,m-1):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][n-1]==1:
                dfs(i,n-1)
        
        return sum(grid[i][j]==1 for i in range(m) for j in range(n))

        
        
