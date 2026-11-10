# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        h = []

        for i in range(len(lists)):
            if not (lists[i] is None):
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        def consume():
            val, i = heapq.heappop(h)
            if not (lists[i] is None):
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
            return ListNode(val)
        
        if not h:
            return None

        head = consume()
        cur = head

        while h:
            nxt = consume()
            cur.next = nxt
            cur = nxt 
            
        return head
