d = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def longest_increasing_path(self, y, x):
        if self.dp[y][x] != -1:
            return self.dp[y][x]
        
        m = 0

        for i in range(len(d)):
            if 0 <= y + d[i][0] < len(self.matrix) and 0 <= x + d[i][1] < len(self.matrix[0]) and self.matrix[y][x] < self.matrix[y + d[i][0]][x + d[i][1]]:
                m = max(m, self.longest_increasing_path(y + d[i][0], x + d[i][1]))

        self.dp[y][x] = m + 1
        return m + 1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        self.matrix = matrix
        self.dp = dp

        m = -1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = max(m, self.longest_increasing_path(i, j))

        return m