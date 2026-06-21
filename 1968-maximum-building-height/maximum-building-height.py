import math

class Solution:
    def update_max_heights(self, i):
        if self.worst[1] + abs(self.r[i][0] - self.worst[0]) <= self.r[i][1]:
            self.max_heights[i] = min(self.max_heights[i], self.worst[1] + abs(self.r[i][0] - self.worst[0]))
        else:
            self.max_heights[i] = min(self.max_heights[i], self.r[i][1])
            self.worst = self.r[i]


    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1

        restrictions.sort()

        self.worst = [1, 0]
        self.r = restrictions
        self.max_heights = [math.inf] * len(self.r)

        for i in range(len(self.r)):
            self.update_max_heights(i)

        worst = [n + 1, math.inf]

        for i in range(len(restrictions) - 1, -1, -1):
            self.update_max_heights(i)

        prev = [1, 0]
        m = 0

        for i in range(len(self.max_heights)):
            x, h = self.r[i][0], self.max_heights[i]
            m = max(m, math.ceil(((x - prev[0] - 1) - abs(h - prev[1])) / 2) + max(prev[1], h))
            prev = [x, h]


        m = max(m, (n - self.r[-1][0]) + self.max_heights[-1])

        return m
