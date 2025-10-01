from functools import lru_cache

class Solution:

    @lru_cache(maxsize=100000)
    def r(self, i, k):
        j = 1

        if i == len(self.stones) - 1:
            return True

        while i + j < len(self.stones) and self.stones[i + j] - self.stones[i] <= k + 1:
            if k - 1 <= self.stones[i + j] - self.stones[i] <= k + 1:
                if self.r(i + j, self.stones[i + j] - self.stones[i]):
                    return True
            j += 1

        return False
        

    def canCross(self, stones: List[int]) -> bool:
        if 1 != stones[1] - stones[0]:
            return False

        self.stones = stones
        return self.r(1, 1)
        