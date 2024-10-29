class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        left = 0
        right = max(max(row) for row in heights)
        m,n = len(heights),len(heights[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        # can we complete the journey with effort x
        def journey(row,col,effort):
            if row==m-1 and col==n-1:
                return True
            
            for dx,dy in dirs:
                nextr, nextc = row+dx, col+dy 
                if (0<=nextr<m) and (0<=nextc<n) and (not (nextr,nextc) in seen) and abs(heights[nextr][nextc]-heights[row][col])<=effort:
                    seen.add((nextr,nextc))
                    if journey(nextr,nextc,effort):
                        return True
            return False
        
        while left <right:
            mid = (left+right) // 2
            seen = set()
            seen.add((0,0))
            if journey(0,0,mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        

       
