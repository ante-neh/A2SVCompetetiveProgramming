# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        def merge(temp1, temp2, cur):
            if not temp1 and not temp2:
                return

            elif not temp2:
                cur.next = temp1
                merge(temp1.next, temp2, cur.next)

            elif not temp1:
                cur.next = temp2
                merge(temp1, temp2.next, cur.next)

            elif temp1.val <= temp2.val:
                cur.next = temp1
                merge(temp1.next, temp2, cur.next)
            
            else:
                cur.next = temp2
                merge(temp1, temp2.next, cur.next)


        merge(list1, list2, cur)

        return dummy.next