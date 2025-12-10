class MyCircularQueue:
    """
    Memory only beats 9%
    """

    def __init__(self, k: int):
        self.head = 0
        self.tail = -1
        self.queue = [-1] * k
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# ## Mock on 3/26/2021
# class MyCircularQueue:
#     '''
#     use 2 stacks to make a queue
#     '''

#     def __init__(self, k: int):
#         self.input = []
#         self.output = []
#         self.k = k
#         self.size = 0

#     def enQueue(self, value: int) -> bool:
#         if self.size < self.k:
#             self.input.append(value)
#             self.size += 1
#             return True
#         else:
#             return False

#     def deQueue(self) -> bool:
#         if self.size == 0:
#             return False
#         else:
#             if self.output:
#                 self.output.pop()
#             else:
#                 while self.input:
#                     self.output.append(self.input.pop())
#                 self.output.pop()
#             self.size -= 1
#             return True


#     def Front(self) -> int:
#         if not self.output:
#             while self.input:
#                 self.output.append(self.input.pop())
#         if not self.size:
#             return -1
#         else:
#             return self.output[-1]

#     def Rear(self) -> int:
#         if not self.size:
#             return -1
#         else:
#             if self.input:
#                 return self.input[-1]
#             elif self.output:
#                 return self.output[0]


#     def isEmpty(self) -> bool:
#         return self.size == 0


#     def isFull(self) -> bool:
#         return self.size == self.k

# # Your MyCircularQueue object will be instantiated and called as such:
# # obj = MyCircularQueue(k)
# # param_1 = obj.enQueue(value)
# # param_2 = obj.deQueue()
# # param_3 = obj.Front()
# # param_4 = obj.Rear()
# # param_5 = obj.isEmpty()
# # param_6 = obj.isFull()


# ## solution on 4/4/2021
# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.q = [-1] * k
#         self.k = k
#         self.head = 0
#         self.tail = -1


#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         else:
#             self.q[(self.tail + 1) % self.k] = value
#             self.tail = (self.tail + 1) % self.k
#             # print(self.q)
#             return True


#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         else:
#             self.q[self.head] = -1
#             self.head = (self.head + 1) % self.k
#             # print(self.q)
#             return True

#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         else:
#             return self.q[self.head]

#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         else:
#             return self.q[self.tail]


#     def isEmpty(self) -> bool:
#         return self.q[self.head] == -1

#     def isFull(self) -> bool:
#         return self.q[(self.tail + 1) % self.k] != -1


# # Your MyCircularQueue object will be instantiated and called as such:
# # obj = MyCircularQueue(k)
# # param_1 = obj.enQueue(value)
# # param_2 = obj.deQueue()
# # param_3 = obj.Front()
# # param_4 = obj.Rear()
# # param_5 = obj.isEmpty()
# # param_6 = obj.isFull()
