class Solution:
    def init(self, val):
        self.val = val
        self.next = None
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head


        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev