class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        trapped = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                trapped += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                trapped += max_r - height[r]

        return trapped
            