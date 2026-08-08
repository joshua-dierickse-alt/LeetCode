DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(y, x, i):
            if board[y][x] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            for dy, dx in DIR:
                ny = y + dy
                nx = x + dx

                if (
                    0 <= ny < len(board) and
                    0 <= nx < len(board[0]) and
                    (ny, nx) not in visited
                ):
                    visited.add((ny, nx))

                    if dfs(ny, nx, i + 1):
                        return True

                    visited.remove((ny, nx))

            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                visited.add((i, j))
                if dfs(i, j, 0):
                    return True
                visited.remove((i, j))

        return False
        