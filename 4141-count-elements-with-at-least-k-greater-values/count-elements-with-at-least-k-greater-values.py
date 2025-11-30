class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        if k == 0:
            return len(nums)

        cutoff = nums[len(nums) - k]

        i = len(nums) - k - 1

        while 0 <= i and nums[i] == cutoff:
            i -= 1
        
        return i + 1