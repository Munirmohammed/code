class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def _addOneRow(root, val, depth_remaining):
            if root is None:
                return
            
            if depth_remaining == 2:
                root.left, root.right = TreeNode(val, left=root.left), TreeNode(val, right=root.right)
                return

            _addOneRow(root.left, val, depth_remaining-1)
            _addOneRow(root.right, val, depth_remaining-1)

        if depth == 1:
            return TreeNode(val, root)

        _addOneRow(root, val, depth)
        return root