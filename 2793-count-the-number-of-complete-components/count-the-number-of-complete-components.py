from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        v = [False] * n
        f = 0

        for i in range(n):
            if v[i]:
                continue
                        
            q = deque([i])
            v[i] = True

            nodes = 0
            edges = 0

            while q:
                node = q.popleft()

                nodes += 1
                edges += len(graph[node])

                for nxt in graph[node]:
                    if not v[nxt]:
                        q.append(nxt)
                        v[nxt] = True

            if nodes * (nodes - 1) == edges:
                f += 1

        return f

