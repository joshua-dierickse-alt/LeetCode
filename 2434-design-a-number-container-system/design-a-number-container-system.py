import heapq
from collections import defaultdict

class NumberContainers:
    def __init__(self):
        self.numbers = {}
        self.heaps = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.numbers[index] = number
        heapq.heappush(self.heaps[number], index)

    def find(self, number: int) -> int:
        heap = self.heaps[number]

        while heap:
            index = heap[0]
            if number == self.numbers[index]:
                return index

            heapq.heappop(heap)

        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)