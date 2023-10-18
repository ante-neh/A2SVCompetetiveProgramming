# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

            if slow == fast:
                break

        slow = head

        while slow and fast:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next

        return False
