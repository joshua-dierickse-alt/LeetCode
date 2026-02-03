import math

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        for i in range(1, len(text1) + 1):
            dp_j1 = dp[0]
            for j in range(1, len(text2) + 1):
                dp_j0 = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = dp_j1 + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                dp_j1 = dp_j0

        return dp[-1]