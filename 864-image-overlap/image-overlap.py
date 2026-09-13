# 30 (1, 30)

# (2 * 30 * 30) ^ 2

DIR = [(1, 1, 0, 0), (0, 1, 1, 0), (1, 0, 0, 1), (0, 0, 1, 1)]

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)

        result = 0

        for d in DIR:
            for i in range(N):
                for j in range(N):
                    matches = 0

                    for a in range(N - i):
                        for b in range(N - j):
                            if img1[a + i*d[0]][b + j*d[1]] == img2[a + i*d[2]][b + j*d[3]] == 1:
                                matches += 1

                    result = max(result, matches)

        return result
        