class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        old_dp = [i for i in range (len(word2) + 1)]
        new_dp = [0] * (len(word2) + 1)

        for i in range(1, len(word1) + 1):
            new_dp[0] = i
            for j in range(1, len(word2) + 1):
                new_dp[j] = min(
                    old_dp[j] + 1,
                    new_dp[j-1] + 1,
                    old_dp[j-1] + (0 if word1[i-1] == word2[j-1] else 1)
                )
            new_dp, old_dp = old_dp, new_dp

        return old_dp[-1]