class Solution:
    def maxDistinct(self, s: str) -> int:
        characters = set()

        for c in s:
            if c not in characters:
                characters.add(c)
                if len(characters) == 26:
                    return 26

        return len(characters)