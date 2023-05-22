class Solution:
        def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if not root:
                return TreeNode(val = val)
            if root.val > val:
                root.left = self.insertIntoBST(root.left, val)
            if root.val < val:
                root.right = self.insertIntoBST(root.right, val)
            return root
            