# class MyHashSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self._range = 10000
#         self.list = [[]]*self._range
        
#     def _hash(self, key: int) -> int:
#         return key%self._range
    
#     def _search(self, key: int) -> int:
#         pool = self.list[self._hash(key)]
#         if len(pool)==0:
#             return -1
#         else:
#             for idx in range(len(pool)):
#                 if pool[idx]==key:
#                     return idx
#             return -1
        
        
#     def add(self, key: int) -> None:
#         if self.contains(key)==False:
#             self.list[self._hash(key)].append(key)
        

#     def remove(self, key: int) -> None:
#         if self.contains(key)==True:
#             idx = self._search(key)
#             self.list[self._hash(key)].pop(idx)
        

#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         if self._search(key)==-1:
#             return False
#         else:
#             return True


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
    
    def _hash(self, key):
        return key % self.keyRange
    
    def add(self, key):
        if not self.contains(key):
            self.bucketArray[self._hash(key)].insert(key)
    
    def remove(self, key):
        if self.contains(key):
            self.bucketArray[self._hash(key)].delete(key)
    
    def contains(self, key):
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
        
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(0) # pseudo head
    
    def insert(self, newValue):
        if not self.exists(newValue): # if not existed, add the new element to the head
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode
            
    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        
    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value==value:
                return True
            curr = curr.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)