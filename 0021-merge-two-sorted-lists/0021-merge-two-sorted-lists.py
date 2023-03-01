# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        def helper(l1, l2, cur):
            if l1 == None and l2 == None:
                return dummy.next
            
            if l1 and not l2:
                cur.next = l1
                return dummy.next
            
            if l2 and not l1:
                cur.next = l2
                return dummy.next
            
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                return helper(l1.next, l2, cur)
            
            else:
                cur.next = l2
                cur = cur.next
                return helper(l1, l2.next,cur)
            
        return helper(list1, list2, dummy)