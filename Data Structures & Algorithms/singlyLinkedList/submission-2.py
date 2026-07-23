class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(val=-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val=val)
        new_head.next = self.head.next
        self.head.next = new_head
        if new_head.next is None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val=val)
        self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and curr.next:
            if i == index:
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr
                return True
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res        
