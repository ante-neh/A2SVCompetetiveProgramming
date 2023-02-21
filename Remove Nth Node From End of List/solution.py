# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        dummy = ListNode()
        prev = dummy

        while cur:
            cur = cur.next
            length += 1
        cur = head
        for i in range(length - n):
            prev.next = cur
            prev = prev.next
            cur = cur.next

        prev.next = cur.next

        return dummy.next