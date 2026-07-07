import math
from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)

        for a, b, d in roads:
            g[a].append((b, d))
            g[b].append((a, d))

        v = set()

        def dfs(n):
            m = math.inf

            for a, d in g[n]:
                if (a, n) not in v:
                    m = min(m, d)

                    v.add((a, n))
                    v.add((n, a))

                    m = min(m, dfs(a))

            return m

        return dfs(1)

            