# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        dummy = ListNode(0, head)
        while n != 1:
            fast = fast.next
            n -= 1

        slow, prev = dummy, dummy
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        prev.next = slow.next

        return dummy.next
