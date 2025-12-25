# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Reverse nodes in groups of k.
        Time: O(n), Space: O(1)
        """
        # Check if we have at least k nodes
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            # Reverse the first k nodes
            reversed_head = self.reverseLinkedList(head, k)
            
            # head now points to the end of the reversed group
            # Recursively reverse the rest and connect
            head.next = self.reverseKGroup(curr, k)
            
            return reversed_head
        
        # Less than k nodes, return as is
        return head
    
    def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
        """
        Reverse first k nodes of the linked list.
        Returns the new head of the reversed portion.
        """
        prev = None
        curr = head
        
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev


# Iterative solution (O(1) space, no recursion stack)
class SolutionIterative:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Iterative approach with O(1) extra space.
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # Check if there are k nodes remaining
            kth = self.getKth(prev_group, k)
            if not kth:
                break
            
            # Save the next group's start
            next_group = kth.next
            
            # Reverse the current group
            prev, curr = kth.next, prev_group.next
            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Connect with previous group
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp
        
        return dummy.next
    
    def getKth(self, curr: ListNode, k: int) -> ListNode:
        """Get the kth node from curr."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


# Helper functions for testing
def create_linked_list(arr):
    """Create a linked list from an array."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_array(head):
    """Convert linked list to array for easy verification."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution_iter = SolutionIterative()
    
    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseKGroup(head1, 2)
    print(f"Test 1: {linked_list_to_array(result1)}")  # [2, 1, 4, 3, 5]
    
    # Test case 2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    result2 = solution.reverseKGroup(head2, 3)
    print(f"Test 2: {linked_list_to_array(result2)}")  # [3, 2, 1, 4, 5]
    
    # Test case 3 - Iterative solution
    head3 = create_linked_list([1, 2, 3, 4, 5])
    result3 = solution_iter.reverseKGroup(head3, 2)
    print(f"Test 3 (Iterative): {linked_list_to_array(result3)}")  # [2, 1, 4, 3, 5]
    
    # Test case 4 - Edge case: k = 1
    head4 = create_linked_list([1, 2, 3])
    result4 = solution.reverseKGroup(head4, 1)
    print(f"Test 4: {linked_list_to_array(result4)}")  # [1, 2, 3]
    
    # Test case 5 - Edge case: k equals list length
    head5 = create_linked_list([1, 2, 3])
    result5 = solution_iter.reverseKGroup(head5, 3)
    print(f"Test 5: {linked_list_to_array(result5)}")  # [3, 2, 1]