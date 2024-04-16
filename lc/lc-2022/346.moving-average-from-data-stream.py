
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.numbers = deque()
        self.size = size
        

    def next(self, val: int) -> float:
        if len(self.numbers) == self.size:
            self.numbers.popleft()
        self.numbers.append(val)
                
        return sum(self.numbers) / len(self.numbers) 

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
