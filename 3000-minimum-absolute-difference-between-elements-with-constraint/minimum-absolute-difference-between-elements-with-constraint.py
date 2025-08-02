import math
import heapq

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0

        for i in range(len(nums)):
            nums[i] = [nums[i], i]

        nums.sort(key=lambda v: v[0])

        heapLeft, heapRight = [], []
        m = math.inf

        for i in range(len(nums)):
            value, index = nums[i]
            heapq.heappush(heapLeft, (index, value))
            heapq.heappush(heapRight, (-index, value))

            while heapLeft and heapLeft[0][0] + x <= index:
                m = min(m, abs(value - heapq.heappop(heapLeft)[1]))
            while heapRight and -heapRight[0][0] >= index + x:
                m = min(m, abs(value - heapq.heappop(heapRight)[1]))

        return m
