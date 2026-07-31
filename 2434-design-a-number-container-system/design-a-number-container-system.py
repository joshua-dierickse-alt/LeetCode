import heapq
from collections import defaultdict

class NumberContainers:
    def __init__(self):
        self.active_values = {}
        self.smallest = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.active_values[index] = number
        heapq.heappush(self.smallest[number], index)

    def find(self, number: int) -> int:
        while self.smallest[number]:
            index = self.smallest[number][0]
            if number == self.active_values[index]:
                return index

            heapq.heappop(self.smallest[number])

        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)