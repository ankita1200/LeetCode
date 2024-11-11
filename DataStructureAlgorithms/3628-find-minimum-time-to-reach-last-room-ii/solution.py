class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m,n = len(moveTime), len(moveTime[0])
        que = [(0,0,0,2)]
        seen = [[False]*n for _ in range(m)]
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        seen[0][0] = True
        while que:
            t,x,y,step = heapq.heappop(que)
            if x==m-1 and y==n-1:
                return t
            for dx,dy in dirs:
                newx, newy = x+dx, y+dy
                if 0<=newx<m and 0<=newy<n and not seen[newx][newy]:
                    seen[newx][newy] = True
                    heapq.heappush(que,(3-step+max(t,moveTime[newx][newy]),newx,newy,3-step))
        
