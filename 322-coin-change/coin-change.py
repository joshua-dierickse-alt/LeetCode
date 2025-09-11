import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [math.inf] * (amount + 1)

        dp[0] = 0

        for i in range(len(dp)):
            if dp[i] != math.inf:
                for j in range(len(coins)):
                    if i + coins[j] <= amount:
                        dp[i + coins[j]] = min(dp[i + coins[j]], dp[i] + 1)

        if dp[len(dp) - 1] == math.inf:
            return -1
        return dp[len(dp) - 1]