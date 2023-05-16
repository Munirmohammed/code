class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next: return head
        head.val, head.next.val = head.next.val, head.val
        self.swapPairs(head.next.next)

        return head