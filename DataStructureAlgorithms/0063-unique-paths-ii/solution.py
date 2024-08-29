class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        
        @cache
        def dp(row,col):
            if row==m-1 and col==n-1:
                return 1 if obstacleGrid[0][0]==0 else 0
            count=0
            if row+1<m and obstacleGrid[row+1][col]==0:
                count = dp(row+1,col)
            if col+1<n and obstacleGrid[row][col+1]==0:
                count += dp(row,col+1)
            return count
        
        return dp(0,0)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
