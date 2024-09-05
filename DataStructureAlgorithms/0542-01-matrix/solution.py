class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = [row for row in mat]
        rows = len(mat)
        cols = len(mat[0])
        queue = deque([])
        seen = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    queue.append((r, c, 0))
                    seen.add((r, c))

        while queue:
            r, c, steps = queue.popleft()
            matrix[r][c] = steps

            for x, y in directions:
                dx = x + r
                dy = y + c

                if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in seen:
                    queue.append((dx, dy, steps + 1))
                    seen.add((dx, dy))

        return matrix


