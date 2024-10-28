class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        left = 0
        right = m*n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid -1
            else:
                left = mid+1
        return False
        
