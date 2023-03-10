# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        dummy = ListNode()
        cur = dummy 
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                

            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next
            
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
            
        return dummy.next
        