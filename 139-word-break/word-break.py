class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}

        for i in range(len(wordDict)):
            temp_ref = trie
            for j in range(len(wordDict[i])):
                if wordDict[i][j] not in temp_ref:
                    temp_ref[wordDict[i][j]] = {}
                temp_ref = temp_ref[wordDict[i][j]]
            temp_ref["0"] = 0
        
        ref_list = [trie]

        for i in range(len(s)):
            new_ref_list = []
            for ref in ref_list:
                if s[i] in ref and ref[s[i]] not in new_ref_list:
                    new_ref_list.append(ref[s[i]])
                if "0" in ref and s[i] in trie and trie[s[i]] not in new_ref_list:
                    new_ref_list.append(trie[s[i]])

            ref_list = new_ref_list

        for i in range(len(ref_list)):
            if "0" in ref_list[i]:
                return True
        return False

