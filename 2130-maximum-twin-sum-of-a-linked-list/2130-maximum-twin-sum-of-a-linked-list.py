# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        maxTwinSum = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        prev = None
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        newHead = prev
        
        while newHead and head:
            maxTwinSum = max(maxTwinSum, newHead.val + head.val)
            newHead = newHead.next
            head = head.next
        
        return maxTwinSum
