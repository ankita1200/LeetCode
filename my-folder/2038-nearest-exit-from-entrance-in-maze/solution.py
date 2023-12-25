class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        m=len(maze)
        n=len(maze[0])
        en_row,en_col=entrance
        entrance.append(0)
        queue=deque([tuple(entrance)])
        seen={tuple(entrance)}
        
        def valid(x,y):
            return 0<=x<m and 0<=y<n and maze[x][y]=="."
        
        while queue:
            # action to perform at current node
            x,y,steps=queue.popleft()
            if (x!=en_row or y!=en_col) and (x==m-1 or x==0 or y==n-1 or y==0):
                return steps
            for dx,dy in directions:
                #conditionally add next set of nodes to the queue
                newx,newy=x+dx,y+dy
                if valid(newx,newy) and (newx,newy) not in seen:
                    seen.add((newx,newy))
                    queue.append((newx,newy,steps+1))
        return -1
        
