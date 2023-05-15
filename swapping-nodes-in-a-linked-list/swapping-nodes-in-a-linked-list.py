class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        for _ in range (k - 1):
            cur = cur.next
        first = cur
        sec = head
        while cur.next:
            cur = cur.next
            sec = sec.next
        first.val , sec.val = sec.val, first.val
        return head
        