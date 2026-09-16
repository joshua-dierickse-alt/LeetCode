class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}

        for num in arr1:
            ref = trie
            for c in str(num):
                nxt = ref.get(c, {})
                ref[c] = nxt
                ref = nxt

        result = 0

        for num in arr2:
            ref = trie
            depth = 0
            for c in str(num):
                if c not in ref:
                    break
                ref = ref[c]
                depth += 1
            result = max(result, depth)
        
        return result
