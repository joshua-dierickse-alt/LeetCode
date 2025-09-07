# test

def get_max(nums, dp, j):
    m = 0
    for i in range(j):
        if nums[i] < nums[j]:
            m = max(m, dp[i])
    return m

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = get_max(nums, dp, i) + 1

        return max(dp)
        