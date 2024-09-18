class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        flip = [[False]*n for _ in range(m)]
        if m == 1 and n == 1 and board[0][0]==1:
            board[0][0]=0
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        for i in range(m):
            for j in range(n):
                count=0
                for dx,dy in dirs:
                    neighborx = i+dx
                    neighbory = j+dy
                    if (0<=neighborx<m) and (0<=neighbory<n) and ((board[neighborx][neighbory]==1 and not flip[neighborx][neighbory]) or (board[neighborx][neighbory]==0 and flip[neighborx][neighbory])):
                        count +=1
                
                if board[i][j]==1 and (count<=1 or count>3):
                    board[i][j]=0
                    flip[i][j]=True

                elif board[i][j]==0 and count==3:
                    board[i][j]=1
                    flip[i][j]=True
                
       
        
                    

        
