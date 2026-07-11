from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        v = [False] * n
        c = 1

        for i in range(n):
            if v[i] != False:
                continue
            
            if i not in graph:
                v[i] = c
                c += 1
                continue
            
            q = deque([i])
            v[i] = c

            while q:
                front = q.popleft()

                for nxt in graph[front]:
                    if v[nxt] == False:
                        q.append(nxt)
                        v[nxt] = c

            c += 1

        def is_complete(component):
            if len(component) == 1:
                return True

            for i in range(len(component) - 1):
                for j in range(i + 1, len(component)):
                    if component[i] not in graph[component[j]]:
                        return False
            return True

        components = defaultdict(list)

        for i, e in enumerate(v):
            components[e].append(i)

        f = 0

        for component in components.values():
            if is_complete(component):
                f += 1

        return f

