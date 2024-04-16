class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, 0))
        else:
            idxCurrMax = self.stack[-1][1]
            if self.stack[idxCurrMax][0] > x:
                self.stack.append((x, idxCurrMax))
            else:
                currLen = len(self.stack)
                self.stack.append((x, currLen))
            

    def pop(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()[0]

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]
        

    def peekMax(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[self.stack[-1][1]][0]
        

    def popMax(self) -> int:
        idxCurrMax = self.stack[-1][1]
        currMax = self.stack[idxCurrMax][0]
        if idxCurrMax == len(self.stack) - 1:
            self.stack.pop()
        else:
            tmp = [self.stack.pop() for i in range(len(self.stack) - 1, idxCurrMax, -1)]
            self.stack.pop() # remove the currMax
            tmp_len = len(tmp)
            for i in range(tmp_len):
                self.push(tmp.pop()[0])
        
        return currMax
    


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
