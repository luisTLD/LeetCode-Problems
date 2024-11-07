# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
            
        return self._reverseList(None, head)
    
    def _reverseList(self, prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
        if curr is None:
            return prev

        next_node = curr.next
        curr.next = prev
        return self._reverseList(curr, next_node)