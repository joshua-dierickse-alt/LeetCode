class Solution:
    def maxProduct(self, n: int) -> int:
        m1, m2 = 0, 0

        for c in str(n):
            c = int(c)

            if c >= m1:
                m1, m2 = c, m1
            elif c >= m2:
                m2 = c

        return m1 * m2

