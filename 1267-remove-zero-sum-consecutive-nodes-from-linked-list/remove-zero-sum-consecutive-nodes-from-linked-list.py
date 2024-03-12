class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        ans=0
        dict_={ans:dummy}
        while head:
            ans+=head.val
            dict_[ans]=head
            head=head.next
        head=dummy
        ans=0
        while head:
            ans+=head.val
            head.next=dict_[ans].next
            head=head.next
        return dummy.next        
        