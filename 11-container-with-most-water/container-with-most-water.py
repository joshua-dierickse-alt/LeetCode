class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        L = height[l]
        R = height[r]

        result = 0

        while l < r:
            result = max(result, (r - l) * min(L, R))
            if L < R:
                l += 1
                L = max(L, height[l])
            else:
                r -= 1
                R = max(R, height[r])

        return result