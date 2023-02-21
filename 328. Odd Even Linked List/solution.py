# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(), ListNode()
        oddHead, evenHead = odd, even

        index = 0
        
        while head:
            if index % 2 == 0:
                oddHead.next = head
                oddHead = oddHead.next
            
            else:
                evenHead.next = head
                evenHead = evenHead.next
            
            head = head.next
            index += 1

        oddHead.next = even.next
        evenHead.next = None

        return odd.next