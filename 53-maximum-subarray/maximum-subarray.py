from functools import lru_cache
import math

class Solution:

    @lru_cache(maxsize=None)
    def r(self, i, b):
        if i >= len(self.nums):
            return -math.inf

        if b:
            return max(self.nums[i], self.nums[i] + self.r(i + 1, True))
        else:
            return max(self.r(i, True), self.r(i + 1, False))


    def maxSubArray(self, nums: List[int]) -> int:
        self.nums = nums

        return self.r(0, False)
        
