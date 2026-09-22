import random

class RandomizedSet:
    def __init__(self):
        self.index = {}
        self.set = []

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.index[val] = len(self.set)
        self.set.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        last = self.set[-1]
        i = self.index[val]

        self.set[i] = last
        self.index[last] = i

        del self.index[val]
        self.set.pop()

        return True

    def getRandom(self) -> int:
        return self.set[random.randint(0, len(self.set) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()