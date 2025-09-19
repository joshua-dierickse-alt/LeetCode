import functools

class Solution:
    @functools.lru_cache(maxsize=None)
    def recursion(self, p1, p2):
        if p1 + p2 == len(self.s3):
            return True

        if p1 < len(self.s1) and self.s1[p1] == self.s3[p1 + p2]:
            if self.recursion(p1 + 1, p2):
                return True

        if p2 < len(self.s2) and self.s2[p2] == self.s3[p1 + p2]:
            if self.recursion(p1, p2 + 1):
                return True
        
        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        return self.recursion(0, 0)
        