import math

MOD = 10 ** 9 + 7

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        result = 0
        for i in range(n - k):
            a = k + 1
            b = (n - 1 - k) - i

            result = (result + math.comb(i + k - 1, k - 1) * math.comb(a + b - 1, b)) % MOD

        return result
