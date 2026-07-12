from collections import defaultdict

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        for c, p in enumerate(parent):
            if p != -1:
                graph[c].append(p)
                graph[p].append(c)

        visted = [False] * len(parent)
        visted[0] = True
        
        def dfs(node):
            max_final = 1
            max_final_1 = 0
            max_final_2 = 0

            for nxt in graph[node]:
                if not visted[nxt]:
                    visted[nxt] = True
                    max_f, max_c = dfs(nxt)
                    
                    max_final = max(max_final, max_f)

                    if s[node] != s[nxt]:
                        if max_c > max_final_1:
                            max_final_1, max_final_2 = max_c, max_final_1
                        elif max_c > max_final_2:
                            max_final_2 = max_c
                    
            return (max(max_final, 1 + max_final_1 + max_final_2), max_final_1 + 1)

        return max(dfs(0))