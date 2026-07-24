class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set()

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s.add(nums[i] ^ nums[j])

        f = set()

        for e in s:
            for num in nums:
                f.add(e ^ num)

        return len(f)