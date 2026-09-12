class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.i = 0
        self.j = 0
        self.encoding = encoding
        
    def next(self, n: int) -> int:
        self.i += n - 1

        while self.j < len(self.encoding):
            if self.encoding[self.j] <= self.i:
                self.i -= self.encoding[self.j]
                self.j += 2
            else:
                self.i += 1
                return self.encoding[self.j + 1]

        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)