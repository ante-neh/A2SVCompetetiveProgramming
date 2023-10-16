# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        leftStart, rightStart = ListNode(), ListNode()
        left, right = leftStart, rightStart

        while temp:
            if temp.val < x:
                left.next = temp
                left = left.next
            
            else:
                right.next = temp
                right = right.next


            temp = temp.next

        left.next = rightStart.next
        right.next = None
        
        return leftStart.next