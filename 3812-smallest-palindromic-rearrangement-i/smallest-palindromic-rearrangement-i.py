OFFSET = ord("a")

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        letters = [0 for _ in range(26)]

        for c in s:
            letters[ord(c) - OFFSET] += 1

        result = []

        for i in range(26):
            num_front = int(letters[i] / 2)

            result.extend([chr(i + OFFSET)] * num_front)

            letters[i] -= num_front * 2

        mid = ""

        for i in range(26):
            if letters[i] == 1:
                mid = chr(i + OFFSET)
                break

        return "".join(result + [mid] + list(reversed(result)))