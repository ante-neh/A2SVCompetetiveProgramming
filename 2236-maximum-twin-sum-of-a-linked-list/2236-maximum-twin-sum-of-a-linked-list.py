# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head.next, head
        left = head
        maxTwinSum = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        prev = None

        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        right = prev

        while left and right:
            maxTwinSum = max(maxTwinSum, left.val + right.val)
            left = left.next
            right = right.next

        return maxTwinSum

        

