class ListNode:
    def __init__(self, key=None, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.htb = {} # hash table to store key:node map
        self.counter = 0
        
        self.head = ListNode()
        self.tail = ListNode(prev=self.head)
        self.head.next = self.tail
        

    def get(self, key: int) -> int:
        if key not in self.htb:
            return -1
        else:
            self.htb[key].prev.next = self.htb[key].next
            self.htb[key].next.prev = self.htb[key].prev
            self.htb[key].prev = self.head
            self.htb[key].next = self.head.next
            self.head.next.prev = self.htb[key]
            self.head.next = self.htb[key]
            return self.htb[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.htb:
            self.htb[key] = ListNode(key=key, val=value, prev=self.head, next=self.head.next)
            self.head.next = self.htb[key]
            self.htb[key].next.prev = self.htb[key]
            # print(self.head.next.val)
            # print(key, self.head.next.key, self.tail.prev.key)
            
            self.counter += 1
            
            if self.counter > self.cap:
                self.htb.pop(self.tail.prev.key)
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
        else:
            self.htb[key].val = value
            self.htb[key].prev.next = self.htb[key].next
            self.htb[key].next.prev = self.htb[key].prev
            self.htb[key].prev = self.head
            self.htb[key].next = self.head.next
            self.head.next.prev = self.htb[key]
            self.head.next = self.htb[key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
