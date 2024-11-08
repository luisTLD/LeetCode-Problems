# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode(0, head)
        first = new_head
        second = new_head

        while n >= 0:
            first = first.next
            n -= 1

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return new_head.next