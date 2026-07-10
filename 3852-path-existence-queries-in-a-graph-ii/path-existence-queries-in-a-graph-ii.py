import math

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # [(0, 1), (4, 2), (2, 3), (3, 4), (1, 8)]
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])

        max_distance = []

        p = 0

        for i in range(len(sorted_nums)):
            while p < len(sorted_nums) and sorted_nums[p][1] - sorted_nums[i][1] <= maxDiff:
                p += 1

            max_distance.append([p - 1 if p - 1 != i else -1])

        log = int(math.log2(len(sorted_nums)))

        for _ in range(log):
            for i in range(len(max_distance)):
                if max_distance[i][-1] != -1:
                    max_distance[i].append(max_distance[max_distance[i][-1]][-1])
                else:
                    max_distance[i].append(-1)

        f = []
        m = {}

        for i in range(len(sorted_nums)):
            m[sorted_nums[i][0]] = i
        
        for l, r in queries:
            l, r = m[l], m[r]
            l, r = min(l, r), max(l, r)

            d = 0
            con = True

            while con and l < r:
                con = False
                for i in range(log, -1, -1):
                    if max_distance[l][i] != -1 and max_distance[l][i] < r:
                        l = max_distance[l][i]
                        d += 2 ** i
                        con = True
                        break

            if l >= r:
                f.append(d)
            elif max_distance[l][0] != -1 and max_distance[l][0] >= r:
                f.append(d + 1)
            else:
                f.append(-1)

        return f

