class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # M[i][m][n] -> given the first i elements, m 0's, and n 1's, this is the max # of i elements we can fit

        def count_01(s):
            zeros = 0
            ones = 0
            for c in s:
                if c == "0":
                    zeros += 1
                else:
                    ones += 1
            return (zeros, ones)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, len(strs) + 1):
            zeros, ones = count_01(strs[i - 1])

            for m_i in range(m, zeros - 1, -1):
                for n_i in range(n, ones - 1, -1):
                    dp[m_i][n_i] = max(dp[m_i][n_i], 1 + dp[m_i - zeros][n_i - ones])

        return dp[-1][-1]
        