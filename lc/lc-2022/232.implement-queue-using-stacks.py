#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    def __init__(self):
        self.left = []
        self.right = []

    def push(self, x: int) -> None:
        self.left.append(x)

    def pop(self) -> int:
        self.__left2right()
        return self.right.pop()

    def peek(self) -> int:
        self.__left2right()
        return self.right[-1]

    def empty(self) -> bool:
        return len(self.left) + len(self.right) == 0

    def __left2right(self) -> None:
        if not self.right:
            while self.left:
                self.right.append(self.left.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
