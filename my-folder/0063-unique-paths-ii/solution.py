class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @cache
        def findNumOfPaths(x,y):
            if x > m-1 or y > n-1:
                return 0
            if obstacleGrid[x][y] == 1:
                return 0
            if x==m-1 and y==n-1:
                return 1
            return findNumOfPaths(x+1,y) + findNumOfPaths(x,y+1)

        return findNumOfPaths(0,0)
            
        
