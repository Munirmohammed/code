class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        res=[]
        while(temp):
            res.append(temp.val)
            temp=temp.next
        res.sort()
        print(res)
        new=head
        i=0
        while new:             
            new.val = res[i]  
            i += 1
            new = new.next
        return head