import math

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        As = [0] * (n + 1)
        Bs = [0] * (n + 1)

        for i in range(1, n + 1):
            As[i] = As[i - 1] + 1 if s[i - 1] == "b" else As[i - 1]

        for i in range(n - 1, -1, -1):
            Bs[i] = Bs[i + 1] + 1 if s[i] == "a" else Bs[i + 1]

        result = math.inf
        for i in range(n):
            result = min(As[i] + Bs[i + 1], result)

        return result
        