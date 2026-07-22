class ListNode:
    def __init__(self, val: int, nxt: "ListNode | None" = None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(val=-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.nxt
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.nxt
        return -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val=val)
        new_head.nxt = self.head.nxt
        self.head.nxt = new_head
        if new_head.nxt is None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val=val)
        self.tail.nxt = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while curr and curr.nxt:
            if i == index:
                if curr.nxt == self.tail:
                    self.tail = curr
                curr.nxt = curr.nxt.nxt
                return True
            i += 1
            curr = curr.nxt
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.nxt
        while curr:
            res.append(curr.val)
            curr = curr.nxt
        return res
