import math

STEPS = 3

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [math.inf] * (STEPS + 1)
        dp[0] = 0

        for i in range(n):
            i_mod = i % (STEPS + 1)
            for j in range(i + 1, min(i + STEPS + 1, n + 1)):
                j_mod = j % (STEPS + 1)
                dp[j_mod] = min(dp[j_mod], dp[i_mod] + costs[j-1] + (j - i) ** 2)

            dp[i_mod] = math.inf

        return dp[n % (STEPS + 1)]
