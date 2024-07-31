from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if grid[row][col] == 1:
                return True
            if (row, col) in visited:
                return True

            visited.add((row, col))
            is_closed = True
            for dx, dy in dirs:
                newr, newc = row + dx, col + dy
                if not dfs(newr, newc):
                    is_closed = False
            return is_closed
        
        visited = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if dfs(i, j):
                        ans += 1
        return ans

