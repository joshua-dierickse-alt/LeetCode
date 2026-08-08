class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = 0
        r_max = 0

        result = 0

        while l <= r:
            if l_max < r_max:
                result += max(0, min(l_max, r_max) - height[l])
                l_max = max(l_max, height[l])
                l += 1
            else:
                result += max(0, min(l_max, r_max) - height[r])
                r_max = max(r_max, height[r])
                r -= 1

        return result
