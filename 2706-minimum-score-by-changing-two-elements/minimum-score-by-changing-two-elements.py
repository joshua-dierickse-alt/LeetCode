import heapq

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        max_heap = [-num for num in nums[:3]]
        min_heap = nums[:3]

        heapq.heapify(max_heap)
        heapq.heapify(min_heap)

        it = iter(nums)
        next(it)
        next(it)
        next(it)

        for num in it:
            heapq.heappushpop(max_heap, -num)
            heapq.heappushpop(min_heap, num)

        a, b, c = sorted([-num for num in max_heap])
        x, y, z = sorted(min_heap)

        return min(x - a, y - b, z - c)
        