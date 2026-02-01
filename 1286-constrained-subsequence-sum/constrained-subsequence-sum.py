from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        d = deque([])

        for i in range(len(nums)):
            nums[i] = max(nums[i], nums[i] + (d[0][0] if d else 0))

            while d and d[-1][0] <= nums[i]:
                d.pop()

            if d and d[0][1] <= i - k:
                d.popleft()

            d.append((nums[i], i))

        return max(nums)
