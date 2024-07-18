class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # run the rotting process, by marking the rotten oranges with the timestamp
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def runRottingProcess(timestamp):
            # flag to indicate if the rotting process should be continued
            to_be_continued = False
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == timestamp:
                        # current contaminated cell
                        for d in directions:
                            n_row, n_col = row + d[0], col + d[1]
                            if ROWS > n_row >= 0 and COLS > n_col >= 0:
                                if grid[n_row][n_col] == 1:
                                    # this fresh orange would be contaminated next
                                    grid[n_row][n_col] = timestamp + 1
                                    to_be_continued = True
            return to_be_continued

        timestamp = 2
        while runRottingProcess(timestamp):
            timestamp += 1
        # end of process, to check if there are still fresh oranges left
        for row in grid:
            for cell in row:
                if cell == 1:  # still got a fresh orange left
                    return -1
        # return elapsed minutes if no fresh orange left
        return timestamp - 2
