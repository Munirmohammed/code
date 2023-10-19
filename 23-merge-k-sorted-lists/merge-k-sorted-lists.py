class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        ListNode.__lt__ = lambda self, other: self.val < other.val

        for l in lists:
            if l:
                heappush(minHeap, l)

        dummyHead = head = ListNode()
        while minHeap:
            node = heappop(minHeap)
            head.next = node
            head = head.next
            node = node.next
            if node:
                heappush(minHeap, node)
        return dummyHead.next