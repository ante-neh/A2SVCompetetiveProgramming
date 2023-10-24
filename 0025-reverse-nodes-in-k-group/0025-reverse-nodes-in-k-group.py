# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevHead = dummy
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length += 1

        remainder = length % k
        cur = head
        for i in range((length - remainder) // k):
            count = k
            prev = None

            while cur and count > 0:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                count -= 1

            temp = prevHead.next
            prevHead.next = prev
            prevHead = temp
            prevHead.next = cur

        return dummy.next



            

