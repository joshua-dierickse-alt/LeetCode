import math

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        unique_id = 0
        prev = -math.inf

        for i in range(len(nums)):
            if nums[i] - prev > maxDiff:
                unique_id += 1
            prev = nums[i]
            nums[i] = unique_id

        for i, [u, v] in enumerate(queries):
            u, v = min(u, v), max(u, v)
            queries[i] = nums[u] == nums[v]
        
        return queries