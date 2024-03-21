class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return head

            # Recursively reverse the rest of the list
            new_head = self.reverseList(head.next)

            # Reverse the current node
            head.next.next = head
            head.next = None

            return new_head
                   


