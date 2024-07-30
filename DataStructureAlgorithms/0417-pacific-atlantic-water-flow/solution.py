class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        pacific_queue=deque()
        atlantic_queue=deque()
        for i in range(m):
            pacific_queue.append((i,0))
            atlantic_queue.append((i,n-1))
        for j in range(n):
            pacific_queue.append((0,j))
            atlantic_queue.append((m-1,j))
        
        def bfs(queue):
            reachable=set()
            while queue:
                row,col=queue.popleft()
                reachable.add((row,col))
                for dx,dy in dirs:
                    newr=row+dx
                    newc=col+dy
                    if newr<0 or newr>=m or newc<0 or newc>=n:
                        continue
                    if (newr,newc) in reachable:
                        continue
                    if heights[newr][newc]<heights[row][col]:
                        continue
                    queue.append((newr,newc))
            return reachable
        pacific_reachable=bfs(pacific_queue)
        atlantic_reachable=bfs(atlantic_queue)
        return list(pacific_reachable.intersection(atlantic_reachable))


        
