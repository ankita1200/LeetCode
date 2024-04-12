from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
            
        seen = set()
        m = len(grid)
        n = len(grid[0])
        maxarea = 0
        
        def valid(row,col):
            if row >=0 and row <m and col >=0 and col <n:
                return True
            else:
                return False
        
        def dfs(row,col,area):
            for i,j in directions:
                r = row +i
                c = col +j
                if valid(r,c) and grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))
                    area = dfs(r,c, area +1)
            return area
                    
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row,col) not in seen:
                    seen.add((row,col))
                    area = dfs(row,col,1)
                    maxarea = max(maxarea, area)
        return maxarea
        
