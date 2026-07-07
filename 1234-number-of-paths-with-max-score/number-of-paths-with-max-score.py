class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10 ** 9 + 7

        rows = len(board)
        cols = len(board[0])

        dp = [[(0, 0)] * cols for _ in range(rows)]
        dp[rows - 1][cols - 1] = (0, 1)
        
        board[0] = board[0].replace("E", "0")

        def next_largest(i, j):
            m = (0, 0)
            for dx, dy in [[1, 0], [1, 1], [0, 1]]:
                nx = i + dx
                ny = j + dy
                if nx == rows or ny == cols:
                    continue
                if m[0] < dp[nx][ny][0]:
                    m = dp[nx][ny]
                elif m[0] == dp[nx][ny][0]:
                    m = (m[0], (m[1] + dp[nx][ny][1]) % mod)
            return m

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if board[i][j] != "X" and (i != rows - 1 or j != cols - 1):
                    n = next_largest(i, j)
                    if n[1] > 0:
                        dp[i][j] = (n[0] + int(board[i][j]), n[1])

        
        return list(dp[0][0])