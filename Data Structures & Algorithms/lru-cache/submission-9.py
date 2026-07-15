
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.firstused = ListNode(-1, -1)
        self.lastused = ListNode(-1, -1)
        self.firstused.next = self.lastused
        self.lastused.prev = self.firstused

    def insert(self, node):
        node.prev = self.lastused.prev
        node.next = self.lastused
        self.lastused.next = None
        self.lastused.prev.next = node
        self.lastused.prev = node

    def remove(self, key):
        nd = self.cache[key]
        nd.prev.next = nd.next
        nd.next.prev = nd.prev
        nd.prev = None
        nd.next = None
        


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.firstused.next.key
            self.remove(lru)
            del self.cache[lru]