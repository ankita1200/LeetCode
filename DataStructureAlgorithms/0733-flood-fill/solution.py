class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if len(image) == 0:
            return 
        if image[sr][sc]==color:
            return image
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(image),len(image[0])
        que = [(sr,sc)]
        stcol = image[sr][sc]
        image[sr][sc] = color
        while que:
            size = len(que)
            for _ in range(size):
                currRow,currCol = que.pop()
                for dx,dy in dirs:
                    nextRow = currRow + dx
                    nextCol = currCol + dy
                    if 0<=nextRow<m and 0<=nextCol<n and image[nextRow][nextCol]==stcol:
                        image[nextRow][nextCol]=color
                        que.append((nextRow,nextCol))
        return image
        
