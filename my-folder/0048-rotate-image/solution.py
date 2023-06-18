class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        row = 0
        for row in range(n-1):
            currrow = row
            for col in range(row,n-1-row):
                currcol = col 
                rotate = 0
                temp = matrix[currrow][currcol]
                while rotate < 4:
                    newrow = currcol
                    newcol = n-1-currrow
                    matrix[newrow][newcol], temp = temp, matrix[newrow][newcol]
                    rotate +=1
                    currrow = newrow
                    currcol = newcol
            
            
        
