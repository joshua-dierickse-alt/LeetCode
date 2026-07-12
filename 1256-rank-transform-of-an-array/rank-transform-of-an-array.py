import math

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(enumerate(arr), key=lambda x: x[1])

        rank = [0] * len(arr)

        c = 0
        prev = math.inf
        for i, cur in sorted_arr:
            if prev != cur:
                c += 1
            rank[i] = c
            prev = cur

        return rank