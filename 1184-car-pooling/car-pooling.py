import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])

        in_car = []

        for num, start, end in trips:
            capacity -= num

            heapq.heappush(in_car, (end, num))

            while in_car and in_car[0][0] <= start:
                capacity += in_car[0][1]
                heapq.heappop(in_car)

            if capacity < 0:
                return False

        return True
