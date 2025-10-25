class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 1:
            return False

        dp = [0] * int(s / 2)
        dp[0] = 1

        for i in range(len(nums)):
            num = nums[i]
            for j in range(num, len(dp)):
                if dp[j - num] != 0 and dp[j - num] != i + 1 and dp[j] == 0:
                    dp[j] = i + 1

            if dp[len(dp) - num] != 0 and dp[len(dp) - num] != i + 1:
                return True

        return False
                



