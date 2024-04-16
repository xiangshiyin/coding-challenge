class MovingAverage:
    from collections import deque

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.sizelimit = size
        

    def next(self, val: int) -> float:
        if len(self.queue) == self.sizelimit:
            self.queue.popleft()
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
