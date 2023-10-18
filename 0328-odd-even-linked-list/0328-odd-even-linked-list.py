# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(), ListNode()
        oddHead, evenHead = odd, even
        index  = 0
        temp = head

        while temp:
            if index % 2 == 0:
                odd.next = temp
                odd = odd.next

            else:
                even.next = temp
                even = even.next

            index += 1
            temp = temp.next

        even.next = None
        odd.next = evenHead.next

        return oddHead.next 

