# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if head and not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right = slow.next
        slow.next = None

        leftHalf = self.sortList(head)
        rightHalf = self.sortList(right)
        
        return self.merge(leftHalf, rightHalf)

    def merge(self, list1, list2):
        p1, p2 = list1, list2
        dummy = ListNode()
        cur = dummy
        if not p1:
            return p2

        if not p2:
            return p1

        if not p1 and not p2:
            return None

        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                cur = cur.next
                p1 = p1.next

            else:
                cur.next = p2
                cur = cur.next
                p2 = p2.next

        while p1:
            cur.next = p1
            cur = cur.next
            p1 = p1.next

        while p2:
            cur.next = p2
            cur = cur.next
            p2 = p2.next

        
        return dummy.next




