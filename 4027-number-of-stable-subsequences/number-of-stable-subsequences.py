class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        e1 = 0
        e2 = 0
        o1 = 0
        o2 = 0

        mod = 10 ** 9 + 7

        for num in nums:
            if num % 2 == 0:
                e2 += e1
                e1 += 1 + o1 + o2
                e2 %= mod
                e1 %= mod
            else:
                o2 += o1
                o1 += 1 + e1 + e2
                o2 %= mod
                o1 %= mod
        
        return (e1 + e2 + o1 + o2) % mod
