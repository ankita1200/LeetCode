class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        cols_hits = [0]*n
        maxcount = 0
        for row in range(m):
            for col in range(n):
                if col == 0 or grid[row][col-1]=='W':
                    rowhits = 0
                    for k in range(col,n):
                        if grid[row][k] == 'W':
                            break
                        if grid[row][k] == 'E':
                            rowhits +=1
                
                if row == 0 or grid[row-1][col]=='W':
                    cols_hits[col]=0
                    for r in range(row,m):
                        if grid[r][col] == 'W':
                            break
                        if grid[r][col] == 'E':
                            cols_hits[col] += 1
                if grid[row][col]=='0':
                    maxcount = max(maxcount, rowhits+cols_hits[col])

        return maxcount

                
        
