class ListNode:
    def __init__(self, key=0, nxt=None):
        self.key = key
        self.nxt = nxt

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode() for _ in range(10**4)]

    def get_hash(self, key):
        return key % len(self.hashSet)

    def add(self, key: int) -> None:
        index = self.get_hash(key)
        curr = self.hashSet[index]
        while curr.nxt:
            if curr.nxt.key == key:
                return
            curr = curr.nxt
        curr.nxt = ListNode(key=key)

    def remove(self, key: int) -> None:
        index = self.get_hash(key)
        curr = self.hashSet[index]
        while curr.nxt:
            if curr.nxt.key == key:
                curr.nxt = curr.nxt.nxt
                return
            curr = curr.nxt

    def contains(self, key: int) -> bool:
        index = self.get_hash(key)
        curr = self.hashSet[index]
        while curr.nxt:
            if curr.nxt.key == key:
                return True
            curr = curr.nxt
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)