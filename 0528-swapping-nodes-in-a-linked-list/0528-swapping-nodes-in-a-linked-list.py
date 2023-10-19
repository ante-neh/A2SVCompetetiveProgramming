# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, second, fast = head, head, head

        while fast and k > 1:
            fast = fast.next
            k -= 1

        first = fast

        while fast and fast.next:
            fast = fast.next
            second = second.next

        first.val, second.val = second.val, first.val

        return head
