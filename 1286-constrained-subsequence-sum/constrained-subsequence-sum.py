from sortedcontainers import SortedList

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        avl = SortedList([nums[0]])

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], avl[-1] + nums[i])

            avl.add(nums[i])

            if len(avl) > k:
                avl.remove(nums[i - k])

        return max(nums)
