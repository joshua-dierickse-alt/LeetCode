class Solution:
    def minChanges(self, s: str) -> int:
        result = 0
        
        for i in range(int(len(s) / 2)):
            result += int(s[2 * i]) ^ int(s[2 * i + 1])

        return result
        