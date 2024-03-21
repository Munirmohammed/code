class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Count the number of nodes in the list
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        # Reverse the list using math
        prev = None
        current = head
        for _ in range(count):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev