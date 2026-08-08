from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []

        for left, right, height in buildings:
            points.append((left, -height))
            points.append((right, height))

        points.sort()
        
        result = []

        tallest = SortedList([0])

        prev_height = 0

        for pos, height in points:
            if height < 0:
                tallest.add(-height)
            else:
                tallest.remove(height)

            max_height = tallest[-1]

            if prev_height != max_height:
                result.append([abs(pos), max_height])
                prev_height = max_height
                
        return result


