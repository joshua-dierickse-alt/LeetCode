class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        n = 0

        for num in arr:
            n = min(n + 1, num)

        return n        