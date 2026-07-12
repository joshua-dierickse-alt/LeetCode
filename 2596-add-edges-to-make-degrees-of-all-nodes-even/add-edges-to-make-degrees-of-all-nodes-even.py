from collections import defaultdict

COMBINATIONS = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]

class Solution:
    def isPossible(self, n: int, edge_pairs: List[List[int]]) -> bool:
        degrees = [0] * (n + 1)
        for u, v in edge_pairs:
            degrees[u] += 1
            degrees[v] += 1

        odd_degree = [i for i, d in enumerate(degrees) if d % 2 == 1]
        
        def build_graph():
            graph = defaultdict(set)

            for u, v in edge_pairs:
                if u in odd_degree:
                    graph[u].add(v)
                if v in odd_degree:
                    graph[v].add(u)

            return graph


        match len(odd_degree):
            case 0:
                return True
            case 1:
                return False
            case 2:
                graph = build_graph()

                u, v = odd_degree

                if v not in graph[u]:
                    return True

                if len(graph[u] | graph[v]) < n:
                    return True

                return False
            case 3:
                return False
            case 4:
                graph = build_graph()

                for pairs in COMBINATIONS:
                    u1, v1, u2, v2 = map(lambda i: odd_degree[i], pairs)

                    if u1 not in graph[v1] and u2 not in graph[v2]:
                        return True
                return False
            case _:
                return False