import math
from collections import Counter

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        min_1s = math.inf
        max_0s = 0
        max_20s = 0
        
        def gen():
            first = True
            count = 0
            cur = s[0]

            for c in s:
                if c == cur:
                    count += 1
                    continue

                if not (first and cur == "1"):
                    yield count
                
                first = False
                cur = c
                count = 1

            if cur == "0":
                yield count

        prev_0s = 0
        max_0 = 0
        max_0s = 0
        min_1s = math.inf


        for i, num in enumerate(gen()):
            if i % 2 == 0:
                max_0s = max(max_0s, prev_0s + num)
                prev_0s = num
                max_0 = max(max_0, num)
            else:
                min_1s = min(min_1s, num)

        ones = s.count("1")

        if min_1s == math.inf:
            return ones

        return max(ones + max_0s, ones + max_0 - min_1s)

