class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        h = {}

        for num in nums:
            h[num] = h.get(num, 0) + 1

        m = 1
        v = {}

        def depth(num):
            if num in v:
                return v[num]
            elif num not in h:
                return -1
            elif num in h and h[num] == 1:
                return 1
            else:
                d = depth(num ** 2)
                v[num] = 2 + depth(num ** 2) if d != -1 else 1
                return v[num]

        for num in nums:
            if num != 1:
                m = max(m, depth(num))

        ones = h.get(1, 1)
        ones = ones - 1 if ones % 2 == 0 else ones

        return max(ones, m)                                               
