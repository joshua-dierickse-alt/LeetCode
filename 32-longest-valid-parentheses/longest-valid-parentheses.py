class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)

        stack = []

        for i in range(len(s)):
            if not stack and s[i] == ")":
                continue
            elif s[i] == ")":
                dp[stack[len(stack) - 1]] = 1
                dp[i] = 1
                stack.pop()
            else:
                stack.append(i)

        m = 0
        c = 0

        for i in range(len(dp)):
            c = c + 1 if dp[i] == 1 else 0
            m = max(m, c)

        return m

