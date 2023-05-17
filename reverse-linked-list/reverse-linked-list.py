class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        while head:
            temp2 = head.next
            head.next = temp
            temp = head
            head = temp2
        return temp