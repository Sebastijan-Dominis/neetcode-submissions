class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None):
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
            i += 1
            curr = curr.next
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
        prev = None
        curr = self.head.next

        while curr:
            if i == index:
                if prev is None:
                    self.head.next = curr.next
                else:
                    prev.next = curr.next
                
                if curr == self.tail:
                    self.tail = prev if prev is not None else self.head

                return True

            i += 1
            prev, curr = curr, curr.next
        
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res        
