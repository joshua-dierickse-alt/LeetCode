from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        frequency = Counter(nums)
        result = []
        scratch_array = []

        def dfs():
            if len(scratch_array) == len(nums):
                result.append(scratch_array.copy())
                return

            for num, freq in frequency.items():
                if freq > 0:
                    frequency[num] -= 1
                    scratch_array.append(num)
                    dfs()
                    scratch_array.pop()
                    frequency[num] += 1

        dfs()

        return result
