import math
from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key=lambda building: (building[0], -building[2]))
        
        result = []

        # (right, height)
        right_corners = SortedList([(math.inf, 0)])

        for left, right, height in buildings:
            while len(right_corners) >= 2 and (right_corner := right_corners[0][0]) < left:
                lower_height = right_corners[1][1]
                result.append([right_corner, lower_height])
                del right_corners[0]

            if height > right_corners[0][1]:
                result.append([left, height])

                if left == right_corners[0][0]:
                    del right_corners[0]

            idx = right_corners.bisect_left((right, -math.inf))

            if height <= right_corners[idx][1]:
                continue

            if right < right_corners[idx][0]:
                idx -= 1

            while idx >= 0 and right_corners[idx][0] <= right and right_corners[idx][1] <= height:
                del right_corners[idx]
                idx -= 1

            right_corners.add((right, height))

        while len(right_corners) >= 2:
            right_corner = right_corners[0][0]
            lower_height = right_corners[1][1]
            result.append([right_corner, lower_height])
            del right_corners[0]

        return result


