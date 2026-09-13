class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)

        for i in range(len(nums)):
            dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])

        return dp[-1]