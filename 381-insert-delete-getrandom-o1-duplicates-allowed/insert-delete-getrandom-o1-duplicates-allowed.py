import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.indexes = defaultdict(set)
        self.elements = []
        
    def insert(self, val: int) -> bool:
        self.elements.append(val)
        self.indexes[val].add(len(self.elements) - 1)
        return len(self.indexes[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.indexes[val]:
            return False

        idx = self.indexes[val].pop()

        last = self.elements.pop()
        
        if idx < len(self.elements):
            self.elements[idx] = last

            self.indexes[last].remove(len(self.elements))
            self.indexes[last].add(idx)

        return True
        
    def getRandom(self) -> int:
        return self.elements[random.randint(0, len(self.elements) - 1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()