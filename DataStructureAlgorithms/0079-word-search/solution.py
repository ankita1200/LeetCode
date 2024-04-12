class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        steps=[(0,1),(1,0),(-1,0),(0,-1)]
        seen=set()
        m=len(board)
        n=len(board[0])
        seen= set()
        w=len(word)
        def checkvalid(x,y):
            return 0<=x<m and 0<=y<n and (x,y) not in seen

        def dfs(x,y,curr):
            seen.add((x,y))
            if curr==w:
                return True
            
            for dx, dy in steps:
                newx=x+dx
                newy=y+dy
                if checkvalid(newx,newy) and board[newx][newy]==word[curr]:
                    outcome=dfs(newx,newy,curr+1)
                    if outcome:
                        return True
                    else:
                        seen.remove((newx,newy))        
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    seen=set()
                    if dfs(i,j,1):
                        return True
        return False
        
