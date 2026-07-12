COMBINATIONS = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]


class Solution:
    def isPossible(self, n: int, edge_pairs: List[List[int]]) -> bool:
        graph = {i + 1: set() for i in range(n)}

        for u, v in edge_pairs:
            graph[u].add(v)
            graph[v].add(u)

        odd_degree = []

        for node, edge in graph.items():
            if len(edge) % 2 == 1:
                odd_degree.append(node)

        match len(odd_degree):
            case 0:
                return True
            case 1:
                return False
            case 2:
                u, v = odd_degree

                if v not in graph[u]:
                    return True

                if len(graph[u] | graph[v]) < n:
                    return True

                return False
            case 3:
                return False
            case 4:
                for pairs in COMBINATIONS:
                    u1, v1, u2, v2 = map(lambda i: odd_degree[i], pairs)

                    if u1 not in graph[v1] and u2 not in graph[v2]:
                        return True
                return False
            case _:
                return False