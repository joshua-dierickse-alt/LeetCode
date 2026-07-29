from sortedcontainers import SortedList

# 1 2 2 2 3
#   ^     ^

class MyCalendar:
    def __init__(self):
        self.bookings = SortedList()
        
    def book(self, startTime: int, endTime: int) -> bool:
        t = (startTime, endTime)

        idx = self.bookings.bisect_right(t)

        if idx < len(self.bookings) and self.bookings[idx][0] < endTime:
            return False

        if 0 <= idx - 1 and startTime < self.bookings[idx - 1][1]:
            return False

        self.bookings.add(t)
        return True

    

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)