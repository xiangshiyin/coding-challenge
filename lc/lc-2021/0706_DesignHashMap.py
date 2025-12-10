# '''
# The Array implementation in Python
# '''

# class Bucket:
#     def __init__(self):
#         self.bucket = []

#     def get(self, key):
#         for (k,v) in self.bucket:
#             if k==key:
#                 return v
#         return -1

#     def update(self, key, value):
#         found = False
#         for i, kv in enumerate(self.bucket):
#             if key == kv[0]:
#                 self.bucket[i] = (key, value)
#                 found = True
#                 return
#         if not found:
#             self.bucket.append((key, value))

#     def remove(self, key):
#         for i, kv in enumerate(self.bucket):
#             if key==kv[0]:
#                 del self.bucket[i]

# class MyHashMap:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.bucketRange = 2069
#         self.bucketArray = [Bucket() for i in range(self.bucketRange)]

#     def _hash(self, key):
#         return key % self.bucketRange


#     def put(self, key: int, value: int) -> None:
#         """
#         value will always be non-negative.
#         """
#         bucketIndex = self._hash(key)
#         self.bucketArray[bucketIndex].update(key,value)


#     def get(self, key: int) -> int:
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         """
#         bucketIndex = self._hash(key)
#         return self.bucketArray[bucketIndex].get(key)


#     def remove(self, key: int) -> None:
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         """
#         bucketIndex = self._hash(key)
#         self.bucketArray[bucketIndex].remove(key)


"""
The LinkedList implementation
"""


class ListNode:
    def __init__(self, key=-1, value=None, nextNode=None):
        self.key = key
        self.value = value
        self.next = nextNode


class MyHashMap:
    def __init__(self):
        self.bucketRange = 2069
        self.bucketList = [ListNode(-1) for _ in range(self.bucketRange)]

    def _hash(self, key):
        return key % self.bucketRange

    def put(self, key: int, value: int) -> None:
        bucketIndex = self._hash(key)
        head = self.bucketList[bucketIndex]
        curr = self.bucketList[bucketIndex].next
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        newNode = ListNode(key, value, head.next)
        head.next = newNode

    def get(self, key: int) -> int:
        bucketIndex = self._hash(key)
        curr = self.bucketList[bucketIndex].next
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        prev = self.bucketList[bucketIndex]
        curr = self.bucketList[bucketIndex].next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
