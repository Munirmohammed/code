class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        totLength = 0
        cur = head

        while cur:
            cur = cur.next
            totLength += 1
        
        cur = head
        for _ in range(totLength // 2):
            cur = cur.next
        
        return cur