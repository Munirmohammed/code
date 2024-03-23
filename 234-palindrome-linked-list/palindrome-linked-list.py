class Solution(object):
    def isPalindrome(self, head):
        reversed_node = None
        fast = slow = head
        while fast and fast.next: 
            fast = fast.next.next
            # reversed_node has the half of head but (reversed)
            reversed_node,reversed_node.next,slow = slow,reversed_node,slow.next
        if fast:
            # Slow catch exact middle of head
            slow = slow.next

        while slow:
            if slow.val != reversed_node.val:
                return False
            else:
                slow = slow.next
                reversed_node = reversed_node.next
        return True