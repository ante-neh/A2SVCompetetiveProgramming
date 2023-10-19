# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        left = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        right = prev

        while right and left:
            rightNext, leftNext = right.next, left.next
            left.next = right
            right.next = leftNext
            right = rightNext
            left = leftNext

        return head



        