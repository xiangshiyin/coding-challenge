class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        

    def push(self, x: int) -> None:
        if len(self.list) == 0:
            self.list.append((x, x))
        else:
            self.list.append((x, min(x, self.getMin())))
        

    def pop(self) -> None:
        self.list.pop()
        

    def top(self) -> int:
        return self.list[-1][0]
        

    def getMin(self) -> int:
        if len(self.list) == 0:
            return None
        else:
            return self.list[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()