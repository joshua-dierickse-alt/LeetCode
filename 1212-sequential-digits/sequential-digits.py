class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = [int(c) for c in str(low)]
        n_old = len(l)
        high = [int(c) for c in str(high)]
        low = [0] * (len(high) - len(l)) + l

        n = len(low)
        result = []

        def sequential(s, n):
            acc = 0
            for i in range(n):
                acc *= 10
                acc += s + i
            result.append(acc)

        def is_high_increasing():
            prev = high[0] - 1
            for d in high:
                if d >= prev + 2:
                    return 1
                if d <= prev:
                    return 0
                prev = d
            return 1

        def is_low_increasing():
            prev = l[0] - 1
            for d in l:
                if d <= prev:
                    return 0
                if d >= prev + 2:
                    return 1
                prev = d

            return 0

        for k in range(n - n_old, -1, -1):
            n_new = n - k

            bottom = 1
            if k == n - n_old:
                bottom = max(bottom, low[k] + is_low_increasing())

            top = min(9, 11 - n_new)
            if k == 0:
                top = min(top, high[0] + is_high_increasing())

            for i in range(bottom, top):
                sequential(i, n_new)
 
        return result