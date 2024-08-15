class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        que = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    que.append((i,j,0))
                    seen.add((i,j))
        while que:
            row,col,steps = que.popleft()
            for dx,dy in dirs:
                nrow=row+dx
                ncol=col+dy
                if (0<=nrow<m) and (0<=ncol<n) and (nrow,ncol) not in seen:
                    seen.add((nrow,ncol))
                    mat[nrow][ncol] = steps+1
                    que.append((nrow,ncol,steps+1))
        return mat
            

        

        
