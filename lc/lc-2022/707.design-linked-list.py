#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start

"""
["MyLinkedList","addAtHead","addAtIndex","get","addAtHead","addAtTail","get","addAtTail","get","addAtHead","get","addAtHead"]
[[],[5],[1,2],[1],[6],[2],[3],[1],[5],[2],[2],[6]]
"""


class Node:
    def __init__(self, val: int = 0, next: "Node" = None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size or self.head is None:
            return -1

        node = self.head
        for i in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        newHead = Node(val=val, next=self.head)
        self.head = newHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newTail = Node(val=val)
        if self.size == 0:
            self.head = newTail
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = newTail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self.size:
            if index == 0:
                self.addAtHead(val=val)
            elif index == self.size:
                self.addAtTail(val=val)
            else:
                p = 0
                node = self.head
                while p < index - 1:
                    node = node.next
                    p += 1
                newNode = Node(val=val, next=node.next)
                node.next = newNode
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                p = 0
                node = self.head
                while p < index - 1:
                    node = node.next
                    p += 1
                node.next = node.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
