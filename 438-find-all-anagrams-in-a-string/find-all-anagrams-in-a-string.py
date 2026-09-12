class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        characters = [0 for _ in range(26)]

        for i in range(len(p)):
            characters[ord(p[i]) - ord("a")] += 1
            characters[ord(s[i]) - ord("a")] -= 1


        def num_zeros(indexes):
            zeros = 0

            for idx in indexes:
                if characters[idx] == 0:
                    zeros += 1

            return zeros

        zeros = num_zeros(range(26))

        result = []

        for i in range(len(s) - len(p)):
            if zeros == 26:
                result.append(i)

            idx1 = ord(s[i]) - ord("a")
            idx2 = ord(s[i + len(p)]) - ord("a")

            zeros_1 = num_zeros([idx1, idx2])

            characters[idx1] += 1
            characters[idx2] -= 1

            zeros_2 = num_zeros([idx1, idx2])

            zeros += zeros_2 - zeros_1
            
        if zeros == 26:
            result.append(len(s) - len(p))

        return result

            
        