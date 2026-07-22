class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = ListNode(val=-1)
        self.tail = ListNode(val=-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail;

    def append(self, value: int) -> None:
        new_node = ListNode(val=value)
        prev = self.tail.prev
        
        new_node.prev = prev
        prev.next = new_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(val=value)
        next = self.head.next

        new_node.next = next
        next.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        target = self.tail.prev
        value = target.val
        prev = target.prev

        self.tail.prev = prev
        prev.next = self.tail
        
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        target = self.head.next
        value = target.val
        next = target.next

        self.head.next = next
        next.prev = self.head

        return value