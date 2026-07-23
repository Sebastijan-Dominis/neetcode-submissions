class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = ListNode(val=-1)
        self.tail = ListNode(val=-1, prev=self.head)
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        return self.head.next == self.tail and self.tail.prev == self.head

    def append(self, value: int) -> None:
        new_tail = ListNode(val=value, prev=self.tail.prev, next=self.tail)
        self.tail.prev.next = new_tail
        self.tail.prev = new_tail

    def appendleft(self, value: int) -> None:
        new_head = ListNode(val=value, prev=self.head, next=self.head.next)
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
