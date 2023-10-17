# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow, prev = dummy, dummy, dummy

        while n > 0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        prev.next = slow.next

        return dummy.next