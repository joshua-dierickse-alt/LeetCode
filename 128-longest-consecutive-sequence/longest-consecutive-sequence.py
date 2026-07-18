from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = [1] * len(nums)
        dsu = [i for i in range(len(nums))]
        
        def find(i):
            if dsu[i] != i:
                dsu[i] = find(dsu[i])
            return dsu[i]

        def union(i, j):
            x, y = find(i), find(j)

            if x == y:
                return
            
            if size[x] < size[y]:
                x, y = y, x

            dsu[y] = x
            size[x] += size[y]


        nums = {nums[i]: i for i in range(len(nums))}

        for num, i in nums.items():
            if num + 1 in nums:
                union(i, nums[num + 1])

        return max(size) if size else 0