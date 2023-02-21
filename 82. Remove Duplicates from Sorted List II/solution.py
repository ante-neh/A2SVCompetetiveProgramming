# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        dummy = ListNode(0,head)
        cur = dummy

        while temp and temp.next:
            if temp and temp.val == temp.next.val:
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next

                cur.next = temp.next
            else:
                cur = cur.next

            temp = temp.next

        return dummy.next