# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow, prev = dummy, dummy, dummy
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        middle = (length // 2) + 1 if length % 2 == 1 else ceil(length / 2)

        while fast and middle > 0:
            fast = fast.next
            middle -= 1

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        prev.next = slow.next

        return dummy.next

        