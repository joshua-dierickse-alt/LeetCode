import math

class Solution:
    def get(self, i):
        return -math.inf if i == -1 or i == len(self.nums) else self.nums[i]

    def rising(self, i):
        return "left" if self.get(i) > self.get(i + 1) else "right"

    def is_peak(self, i):
        return  self.get(i - 1) < self.get(i) > self.get(i + 1)

    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        self.nums = nums

        while l < r - 1:
            m = l + int((r - l) / 2)

            if self.rising(m) == "right":
                l = m
            else:
                r = m

        return l if self.is_peak(l) else r