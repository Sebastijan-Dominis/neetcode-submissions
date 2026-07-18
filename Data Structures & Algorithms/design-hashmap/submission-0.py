class ListNode:
    def __init__(self, key=-1, val=-1, nxt=None):
        self.key = key
        self.val = val
        self.nxt = nxt

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode() for _ in range(10**4)]

    def get_hash(self, key):
        return key % len(self.hashMap)

    def put(self, key: int, value: int) -> None:
        index = self.get_hash(key)
        curr = self.hashMap[index]
        while curr.nxt:
            if curr.nxt.key == key:
                curr.nxt.val = value
                return
            curr = curr.nxt
        curr.nxt = ListNode(key=key, val=value, nxt=None)

    def get(self, key: int) -> int:
        index = self.get_hash(key)
        curr = self.hashMap[index]
        while curr.nxt:
            if curr.nxt.key == key:
                return curr.nxt.val
            curr = curr.nxt
        return -1

    def remove(self, key: int) -> None:
        index = self.get_hash(key)
        curr = self.hashMap[index]
        while curr.nxt:
            if curr.nxt.key == key:
                curr.nxt = curr.nxt.nxt
                return
            curr = curr.nxt


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)