# 346. Moving Average from Data Stream
# 8 mins to solve

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAverage:

    def __init__(self, size: int):
        self.items = []
        self.size = size

    def next(self, val: int) -> float:
        if len(self.items) >= self.size:
            self.items.pop(0)
            
        self.items.append(val)
        return sum(self.items)/len(self.items)

# pop oldest - O(n)
# Sum computation - O(n)
# Per call complexity - O(n)

# Better Solution 
class MovingAverage:

    def __init__(self, size: int):

        self.total = 0
        self.len = 0

        self.q = deque([])

        self.size = size
        

    def next(self, val: int) -> float:

        self.q.append(val)

        self.total += val

        self.len += 1

        if self.len > self.size:
            self.total -= self.q.popleft()
            self.len -= 1

        return self.total / self.len

# pop oldest - O(1)
# Sum computation - O(1)
# Per call complexity - O(1)