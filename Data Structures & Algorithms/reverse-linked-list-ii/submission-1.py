# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        preStart = dummy
        start = head
        for _ in range(left-1):
            preStart, start = start, start.next
        
        prev = None
        end = start
        for _ in range(left, right+1):
            tmp = end.next
            end.next = prev
            prev = end
            end = tmp
        
        preStart.next = prev
        start.next = end
        return dummy.next