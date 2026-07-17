class MyCircularQueue:
    def __init__(self, k: int):
        self.e = 0
        self.k = k
        self.queue = [None] * k
        self.front = 0
        self.back = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.front] = value
        self.front = (self.front + 1) % self.k
        self.e += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.back = (self.back + 1) % self.k
        self.e -= 1

        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.back]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front - 1]

    def isEmpty(self) -> bool:
        return self.e == 0

    def isFull(self) -> bool:
        return self.e == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()