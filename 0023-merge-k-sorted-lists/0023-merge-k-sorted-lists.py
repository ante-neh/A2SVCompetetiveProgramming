# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.merge(list1, list2))

            lists = mergedList

        return lists[0]

    def merge(self, list1, list2):
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next

            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next

        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next

        return dummy.next
        
