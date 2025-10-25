import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = -math.inf

        c = 0

        for num in nums:
            c += num
            m = max(m, c)
            c = max(c, 0)

        return m