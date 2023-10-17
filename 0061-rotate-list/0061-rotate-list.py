# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head
        prev = None
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1
        
        k = k % n
        if k == 0:
            return head
            
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            n += 1

        leftStart = prev
        current = prev
        prev = None


        while k > 0 and current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            k -= 1

        newHead = prev
        prev = None 

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        leftStart.next = prev

        return newHead


