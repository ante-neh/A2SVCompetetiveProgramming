# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        temp = dummy

        leftPrev, rightPrev, leftNode = dummy, dummy, dummy
        i = 0

        while i < left and temp:
            leftPrev = temp
            temp = temp.next
            i += 1

        leftNode = temp

        temp = dummy
        i = 0

        while i < right and temp:
            temp = temp.next
            i += 1

        rightNode = temp

        current = leftNode
        prev = None

        count = right - left + 1

        while current and count > 0:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            count -= 1

        leftPrev.next = rightNode
        leftNode.next = current

        return dummy.next 
        