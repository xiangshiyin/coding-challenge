class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque

        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        q = self.q1 if len(self.q1) == 0 else self.q2  # q is the empty queue
        Q = self.q2 if len(self.q1) == 0 else self.q1  # Q is the non-empty queue
        q.append(x)  # append the new element
        # transfer all elements from Q to q
        while Q:
            q.append(Q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        Q = self.q1 if len(self.q1) > 0 else self.q2
        return Q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        Q = self.q1 if len(self.q1) > 0 else self.q2
        return Q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0 and len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
