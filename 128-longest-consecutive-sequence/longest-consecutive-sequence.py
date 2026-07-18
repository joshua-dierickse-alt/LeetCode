class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = {num: False for num in nums}

        longest = 0
        for num, visited in s.items():
            d = 1
            if not visited:
                s[num] = True
                i = 1
                while num - i in s:
                    s[num - i] = True
                    i += 1
                    d += 1

                i = 1
                while num + i in s:
                    s[num + i] = True
                    i += 1
                    d += 1
            
            longest = max(longest, d)

        return longest