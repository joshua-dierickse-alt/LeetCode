class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        result = 0

        points = [
            (i, j)
            for i in range(N)
            for j in range(N)
            if img1[i][j]
        ]

        for di in range(-N + 1, N):
            for dj in range(-N + 1, N):
                matches = 0

                for i, j in points:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < N and 0 <= nj < N:
                        matches += img2[ni][nj]

                result = max(result, matches)

        return result