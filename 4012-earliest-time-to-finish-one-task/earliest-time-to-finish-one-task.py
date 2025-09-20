import math

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        m = math.inf
        for i in range(len(tasks)):
            m = min(m, tasks[i][0] + tasks[i][1])

        return m