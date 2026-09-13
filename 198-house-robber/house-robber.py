class Solution:
    def rob(self, nums: List[int]) -> int:
        house1 = 0
        house2 = 0

        for i in range(len(nums)):
            house2, house1 = max(house2, house1 + nums[i]), house2

        return house2