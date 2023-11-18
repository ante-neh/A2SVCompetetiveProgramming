# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        temp = head
        curSum = 0

        while temp:
            if temp.val == 0:
                cur.next = ListNode(curSum)
                cur = cur.next
                curSum = 0

            curSum += temp.val
            temp = temp.next

        return dummy.next.next

