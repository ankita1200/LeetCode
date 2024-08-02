class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n=len(rooms),len(rooms[0])
        queue=deque()
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    queue.append((i,j,0))
                  
        seen=set()
        while queue:
            load=len(queue)
            for it in range(load):
                row,col,dist=queue.popleft()
                for dx,dy in dirs:
                    newr=row+dx
                    newc=col+dy
                    if newr<0 or newr>=m or newc<0 or newc>=n:
                        continue
                    if rooms[newr][newc]==-1 or rooms[newr][newc]==0:
                        continue
                    if not (newr,newc) in seen:
                        rooms[newr][newc]=dist+1
                        queue.append((newr,newc,dist+1))
                        seen.add((newr,newc))
                



        
