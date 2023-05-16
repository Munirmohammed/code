class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {}
    
        while (head):
            if head.next not in nodes:
                nodes[head.next] = 1
            else:
                return True
            head = head.next

        return False