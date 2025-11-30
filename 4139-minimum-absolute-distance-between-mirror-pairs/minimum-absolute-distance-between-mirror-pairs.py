import math
from functools import lru_cache

@lru_cache(maxsize=None)
def reverse(i):
    s = str(i)

    ns = ""

    for c in s:
        ns = c + ns

    return int(ns)

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        m = {}

        a = math.inf

        for i in range(len(nums)):
            if nums[i] in m:
                a = min(a, abs(i - m[nums[i]]))

            m[reverse(nums[i])] = i

        return -1 if a == math.inf else a