from itertools import product
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = [[False]*n for _ in range(m)]
        que = deque()
        borders = list(product(range(m),[0,n-1])) + list(product([0,m-1],range(n)))
        for row,col in borders:
            if board[row][col]=="O" and not visited[row][col]:
                visited[row][col]=True
                que.append((row,col))
        while que:
            row,col = que.popleft()
            for dx,dy in dirs:
                newx,newy = row+dx,col+dy
                if 0<=newx<m and 0<=newy<n and board[newx][newy]=="O" and not visited[newx][newy]:
                    visited[newx][newy]=True
                    que.append((newx,newy))
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and not visited[i][j]:
                    board[i][j]="X"
    




