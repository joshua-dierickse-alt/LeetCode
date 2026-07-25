class Solution:
    def maxProduct(self, n: int) -> int:
        arr = [0] * 10

        for c in str(n):
            arr[ord(c) - ord("0")] += 1

        m = None

        for i in range(9, -1, -1):
            if m is None and arr[i] >= 2:
                return i ** 2
            elif arr[i] >= 1:
                if m is None:
                    m = i
                else:
                    return i * m
