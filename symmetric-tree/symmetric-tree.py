class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSmallSymmetric(a,b):
            if type(a)==TreeNode and type(b)==TreeNode:
                if a.val==b.val:
                    return isSmallSymmetric(a.left,b.right) and isSmallSymmetric(a.right,b.left)
            else:
                return a==b
        return isSmallSymmetric(root.left,root.right)