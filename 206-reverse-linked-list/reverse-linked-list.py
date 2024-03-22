class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head


        class Node:
            def __init__(self, val):
                self.val = val
                self.next = None

        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Create a new node and assign the reversed list to it
        new_head = Node(None)
        reversed_list = prev

        curr = new_head
        while reversed_list:
            curr.next = Node(reversed_list.val)
            reversed_list = reversed_list.next
            curr = curr.next

        return new_head.next