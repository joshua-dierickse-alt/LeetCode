from collections import defaultdict

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = [[] for _ in range(len(s))]

        it = enumerate(parent)
        next(it)

        for c, p in it:
            graph[p].append(c)

        res = [0]
        
        def dfs(node):
            max_1 = 0
            max_2 = 0

            for nxt in graph[node]:
                max_r = dfs(nxt)
                
                if s[node] != s[nxt]:
                    if max_r > max_1:
                        max_1, max_2 = max_r, max_1
                    elif max_r > max_2:
                        max_2 = max_r
            
            res[0] = max(res[0], max_1 + max_2 + 1)

            return max_1 + 1

        dfs(0)
        return res[0] 