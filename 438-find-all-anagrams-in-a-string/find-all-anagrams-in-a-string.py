class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        characters = [0 for _ in range(26)]

        for i in range(len(p)):
            characters[ord(p[i]) - ord("a")] += 1
            characters[ord(s[i]) - ord("a")] -= 1

        def is_anagram():
            for val in characters:
                if val != 0:
                    return False
            return True

        result = []

        for i in range(len(s) - len(p)):
            if is_anagram():
                result.append(i)

            characters[ord(s[i]) - ord("a")] += 1
            characters[ord(s[i + len(p)]) - ord("a")] -= 1
            
        if is_anagram():
            result.append(len(s) - len(p))

        return result

            
        