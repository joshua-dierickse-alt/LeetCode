class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        dsu = [i for i in range(rows * cols)]
        size = [1] * (rows * cols)
        border = [i == 0 or j == 0 or i == rows - 1 or j == cols - 1 for i in range(rows) for j in range(cols)]
        region = [board[i][j] for i in range(rows) for j in range(cols)]

        def find(i):
            if i != dsu[i]:
                dsu[i] = find(dsu[i])
            return dsu[i]

        def union(i, j, r = None):
            x, y = find(i), find(j)

            if x == y:
                return

            if size[x] < size[y]:
                x, y = y, x

            dsu[y] = x
            size[x] += size[y]
            border[x] = border[x] or border[y]
            if r is not None:
                region[x] = r

        def flatten(i, j):
            return i * cols + j

        for i in range(rows):
            for j in range(cols):
                if j + 1 < cols and board[i][j] == board[i][j + 1]:
                    union(flatten(i, j), flatten(i, j + 1))
                if i + 1 < rows and board[i][j] == board[i + 1][j]:
                    union(flatten(i + 1, j), flatten(i, j))

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                x = find(flatten(i, j))
                y = find(flatten(i - 1, j))
                if not border[x] and region[x] == "O" and region[y] == "X":
                    union(x, y, "X")

                board[i][j] = region[find(flatten(i, j))]