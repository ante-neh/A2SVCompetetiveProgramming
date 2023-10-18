# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and k > 1:
            fast = fast.next
            k -= 1

        left = fast
        while fast.next:
            fast = fast.next
            slow = slow.next


        slow.val, left.val = left.val, slow.val

        return head