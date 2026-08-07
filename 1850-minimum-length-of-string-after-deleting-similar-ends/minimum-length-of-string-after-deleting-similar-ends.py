class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        while l < r:
            c = s[l]

            if s[r] != c:
                return r - l + 1

            while l < len(s) and c == s[l]:
                l += 1
            
            while 0 <= r and c == s[r]:
                r -= 1

        if l > r:
            return 0

        return r - l + 1
        