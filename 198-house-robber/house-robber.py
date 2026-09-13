class Solution:
    def rob(self, nums: List[int]) -> int:
        house1 = 0
        house2 = 0
        house3 = 0

        for i in range(len(nums)):
            house3 = max(house2, house1 + nums[i])
            house2, house1 = house3, house2

        return house3