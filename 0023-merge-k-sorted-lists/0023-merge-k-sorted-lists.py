# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heappush(heap, head.val)
                head = head.next
             
        mergedList = ListNode()
        cur = mergedList
        
        while heap:
            val = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            
        return mergedList.next