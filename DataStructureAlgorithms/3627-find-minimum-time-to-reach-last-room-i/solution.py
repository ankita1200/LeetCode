class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # we will need to keep frontier cells in a heap priority queue
        # as we progress through time each frontier will expand if it meets time constraint
        m,n = len(moveTime), len(moveTime[0])
        que = [(0,0,0)]
        heapq.heapify(que)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        seen = [[False]*n for _ in range(m)]
        seen[0][0] = True
        while que:
            t,x,y = heapq.heappop(que)
            if x==m-1 and y==n-1:
                return t
            for dx,dy in dirs:
                newx, newy = x+dx, y+dy
                if (0<=newx<m) and (0<=newy<n) and not seen[newx][newy]:
                    seen[newx][newy] = True
                    heapq.heappush(que,(1+max(t,moveTime[newx][newy]),newx,newy))
            
        


        
