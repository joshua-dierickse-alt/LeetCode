class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = nums[0]
        max_num = nums[0]
        for num in nums:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

        for i in range(min_num, 0, -1):
            if min_num % i == 0 and max_num % i == 0:
                return i

        return 1