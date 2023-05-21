class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(root):
            if root:
                root.left,root.right=root.right,root.left
                swap(root.left)
                swap(root.right)
        swap(root)
        return root