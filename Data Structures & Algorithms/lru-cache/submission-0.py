class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left
        self.capacity = capacity

    def delete(self, node: Node) -> None:
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev

        del self.cache[node.key]

    def insert(self, node: Node) -> None:
        right = self.right
        last = right.prev

        last.nxt = node
        right.prev = node
        node.prev = last
        node.nxt = right

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.cache[key] = node
            self.insert(node)
            return node.value
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.cache[key] = node
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.capacity:
                lru = self.left.nxt
                self.delete(lru)