from functools import lru_cache

class Solution:

    @lru_cache(maxsize=100000)
    def r(self, i, k):
        if i == self.n - 1:
            return True
        j = 1
        while i + j < self.n and self.stones[i + j] - self.stones[i] <= k + 1:
            if k - 1 <= self.stones[i + j] - self.stones[i] <= k + 1:
                if self.r(i + j, self.stones[i + j] - self.stones[i]):
                    return True
            j += 1

        return False
        

    def canCross(self, stones: List[int]) -> bool:
        if 1 != stones[1] - stones[0]:
            return False

        self.stones = stones
        self.n = len(self.stones)

        return self.r(1, 1)
        