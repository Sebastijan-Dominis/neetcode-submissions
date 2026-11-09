# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        right -= left
        right += 1
        left -= 1

        preLeft, currLeft = dummy, head
        while left:
            preLeft, currLeft = currLeft, currLeft.next
            left -= 1
        
        prev = None
        currRight = currLeft
        while right:
            tmp = currRight.next
            currRight.next = prev
            prev = currRight
            currRight = tmp
            right -= 1

        preLeft.next = prev
        currLeft.next = currRight
        return dummy.next