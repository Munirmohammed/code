class Solution:
    def findBottomLeftValue(self, r: Optional[TreeNode]) -> int:
        return reduce(lambda _,n:q.extend(filter(None,(n.right,n.left))) or n.val,q:=[r],0)