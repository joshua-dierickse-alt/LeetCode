class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        c = num.bit_length() - 1

        while num > 0:
            num -= num & -num
            c += 1

        return c  

