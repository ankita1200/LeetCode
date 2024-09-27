from collections import defaultdict


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (
                d in rows[row]
                or d in columns[col]
                or d in boxes[box_index(row, col)]
            )

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number that didn't lead to a solution
            """
            rows[row][d] -= 1
            columns[col][d] -= 1
            boxes[box_index(row, col)][d] -= 1
            if rows[row][d] == 0:
                del rows[row][d]
            if columns[col][d] == 0:
                del columns[col][d]
            if boxes[box_index(row, col)][d] == 0:
                del boxes[box_index(row, col)][d]
            board[row][col] = "."

        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion to continue to place numbers
            till the moment we have a solution
            """
            if col == N - 1 and row == N - 1:
                sudoku_solved[0] = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            """
            if board[row][col] == ".":
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if sudoku_solved[0]:
                            return
                        remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        n = 3
        N = n * n
        box_index = lambda row, col: (row // n) * n + col // n

        rows = [defaultdict(int) for _ in range(N)]
        columns = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = [False]
        backtrack()
