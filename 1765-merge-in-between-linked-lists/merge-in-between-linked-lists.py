class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the node before the removal range
        prev = None
        curr = list1
        for _ in range(a):
            prev = curr
            curr = curr.next
        
        # Remove the nodes in the range [a, b]
        next_node = curr.next
        for _ in range(b - a):
            curr.next = next_node
            curr = next_node
            if next_node:
                next_node = next_node.next
        
        # Insert list2 into the removed range
        if prev:
            prev.next = list2
        else:
            list1 = list2
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = next_node
        
        return list1