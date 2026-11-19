class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        nums.sort()

        a, b, c = nums[:3]

        x, y, z = nums[-3:]

        return min(x - a, y - b, z - c)
        