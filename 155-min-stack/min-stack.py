import math

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.min.append(min(value, self.min[-1] if self.min else math.inf))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()