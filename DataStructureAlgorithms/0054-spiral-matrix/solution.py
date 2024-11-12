class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = [(0,1),(1,0),(0,-1),(-1,0)]
        dir = 0
        m,n = len(matrix), len(matrix[0])
        seen = [[False]*n for _ in range(m)]
        count = 0
        x = y = 0
        ans = []
        while count< m*n:
            seen[x][y] = True
            ans.append(matrix[x][y])
            count += 1
            dx,dy = order[dir]
            if (x+dx)<0 or (x+dx)>=m or (y+dy)<0 or (y+dy)>=n or seen[x+dx][y+dy]:
                dir = (dir+1) % 4
                dx,dy = order[dir]
            x += dx
            y += dy
        return ans
            


