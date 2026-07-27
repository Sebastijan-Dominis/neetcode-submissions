class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None, prev: "ListNode | None" = None):
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
        return self.head.next == self.tail and self.tail.prev == self.head

    def append(self, value: int) -> None:
        node = ListNode(val=value)

        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = ListNode(val=value)

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        value = self.tail.prev.val
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        value = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return value
