import random

class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def reset(self) -> list[int]:
        return self.nums

    def shuffle(self) -> list[int]:
        result = self.nums.copy()

        for i in range(len(result) - 1, -1, -1):
            j = random.randint(0, i)
            result[i], result[j] = result[j], result[i]

        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()