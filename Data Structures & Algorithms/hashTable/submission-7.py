class ListNode:
    def __init__(self, key: int, val: int, next: ListNode | None = None):
        self.key = key
        self.val = val
        self.next = next

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0

    def hash_function(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        new_node = ListNode(key, value)
        
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            curr = self.table[index]
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                
                if curr.next is None:
                    curr.next = new_node
                
                curr = curr.next
        
        self.size += 1
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        curr = self.table[index]

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        
        curr = self.table[index]
        prev = None

        while curr:
            if curr.key == key:
                if prev is None:
                    self.table[index] = curr.next
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
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            while node:
                new_node = ListNode(node.key, node.val)
                index = self.hash_function(node.key)
                
                if new_table[index] is None:
                    new_table[index] = new_node
                else:
                    new_node.next = new_table[index]
                    new_table[index] = new_node
                
                node = node.next
        
        self.table = new_table
















