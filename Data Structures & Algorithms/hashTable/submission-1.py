class ListNode:
    def __init__(self, key: int, val: int, next: "ListNode | None" = None):
        self.key = key
        self.val = val
        self.next = next

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0

    def hashing_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hashing_function(key)
        prev = None
        curr = self.table[index]
        new_node = ListNode(key=key, val=value)
        
        if curr is None:
            self.table[index] = new_node
            self.size += 1
        else:
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                prev, curr = curr, curr.next
            prev.next = new_node
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hashing_function(key)
        curr = self.table[index]
        while curr:
            if key == curr.key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hashing_function(key)
        prev = None
        curr = self.table[index]
        if curr is None:
            return False
        
        while curr:
            if curr.key == key:
                if prev is None:
                    self.table[index] = None
                else:
                    prev.next = curr.next
                self.size -= 1
                return True
            prev, curr = curr, curr.next
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                index = self.hashing_function(node.key)
                curr = new_table[index]
                new_node = ListNode(key=node.key, val=node.val)
                if curr is None:
                    new_table[index] = new_node
                else:
                    while curr.next:
                        curr = curr.next
                    curr.next = new_node
            
                node = node.next
        
        self.capacity = new_capacity
        self.table = new_table

































