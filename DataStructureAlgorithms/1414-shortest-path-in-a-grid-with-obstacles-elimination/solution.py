class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        que = deque()
        que.append((0,0,0,k))
        m = len(grid)
        n = len(grid[0])
        seen = set()
        seen.add((0,0,k))

        def isValid(row,col):
            return (0<=row<m) and (0<=col<n)
        
        while que:
            currrow, currcol, steps, remk = que.popleft()
            if (currrow==m-1) and (currcol==n-1):
                return steps
            for dx,dy in dirs:
                nextrow = currrow+dx
                nextcol = currcol+dy
                if isValid(nextrow,nextcol):
                    nextrem = remk - grid[nextrow][nextcol]
                    if nextrem >= 0 and (nextrow,nextcol,nextrem) not in seen:
                        seen.add((nextrow,nextcol,nextrem))
                        que.append((nextrow,nextcol,steps+1,nextrem))
        return -1

        
