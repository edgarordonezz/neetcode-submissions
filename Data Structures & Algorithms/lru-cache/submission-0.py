class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0) # dummy, represents the LRU end
        self.right = Node(0, 0) # dummy, represents the MRU end
        self.left.next = self.right 
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key] # Node object, not just a number
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.left.next # node right next to the LRU sentinel
            self.remove(lru) # unlink from list
            del self.cache[lru.key] # remove it from the hash map too
            
    def remove(self, node: Node):
        prev = node.prev # set previous node
        nxt = node.next # set next node
        prev.next = nxt # prev skips node, points to nxt
        nxt.prev = prev # nxt skips node, points to prev

    def insert(self, node: Node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None