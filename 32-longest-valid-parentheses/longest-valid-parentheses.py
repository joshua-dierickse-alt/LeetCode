class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif stack:
                open_idx = stack.pop()
                dp[open_idx] = dp[i] = 1

        max_len = cur = 0
        for val in dp:
            cur = cur + 1 if val else 0
            max_len = max(max_len, cur)

        return max_len
