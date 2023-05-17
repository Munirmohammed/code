class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = arr2 = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        for i in range(n):
            arr2.append(arr[i]+arr[n-1-i])
        arr.sort()
        return arr[-1]
        