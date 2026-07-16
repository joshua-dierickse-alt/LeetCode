class NumArray:
    def __init__(self, nums: List[int]):
        self.psa = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.psa[i + 1] = self.psa[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.psa[right + 1] - self.psa[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)