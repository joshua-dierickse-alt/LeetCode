from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        f = []
        d = deque()

        for i in range(len(nums)):
            while len(d) > 0 and d[-1][0] <= nums[i]:
                d.pop()

            d.append((nums[i], i))

            if i - d[0][1] >= k:
                d.popleft()
            
            if i >= k - 1:
                f.append(d[0][0])

        return f