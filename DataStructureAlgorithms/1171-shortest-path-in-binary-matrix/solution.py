class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        if grid[0][0]==1:
            return -1
        n = len(grid)
        que = deque([(0,0,1)])
        seen = {(0,0)}
        dirs = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        while que:
            row,col,steps = que.popleft()
            if (row==n-1) and (col==n-1):
                return steps
            for dx,dy in dirs:
                nrow = row+dx
                ncol = col+dy
                if (0<=nrow<n) and (0<=ncol<n) and ((nrow,ncol) not in seen) and (grid[nrow][ncol]==0):
                    que.append((nrow,ncol,steps+1))
                    seen.add((nrow,ncol))
        return -1



        
