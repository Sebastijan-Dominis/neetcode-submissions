class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None, prev: "ListNode | None" = None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail and self.tail.prev == self.head

    def append(self, value: int) -> None:
        new_tail = ListNode(value)
        
        new_tail.prev = self.tail.prev
        new_tail.next = self.tail

        self.tail.prev.next = new_tail
        self.tail.prev = new_tail

    def appendleft(self, value: int) -> None:
        new_head = ListNode(value)

        new_head.next = self.head.next
        new_head.prev = self.head

        self.head.next.prev = new_head
        self.head.next = new_head

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