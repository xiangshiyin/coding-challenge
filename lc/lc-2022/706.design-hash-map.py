#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#


# @lc code=start
class Bucket:
    def __init__(self) -> None:
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        for i, k in enumerate(self.bucket):
            if k[0] == key:
                self.bucket[i] = (key, value)
                return
        self.bucket.append((key, value))

    def remove(self, key):
        for i, k in enumerate(self.bucket):
            if k[0] == key:
                del self.bucket[i]
                return


class MyHashMap:
    def __init__(self):
        self.hashrange = 2048
        self.hashmap = [Bucket() for i in range(self.hashrange)]

    def _hash(self, key):
        return key % self.hashrange

    def put(self, key: int, value: int) -> None:
        hashkey = self._hash(key)
        self.hashmap[hashkey].update(key, value)

    def get(self, key: int) -> int:
        hashkey = self._hash(key)
        return self.hashmap[hashkey].get(key)

    def remove(self, key: int) -> None:
        hashkey = self._hash(key)
        self.hashmap[hashkey].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
