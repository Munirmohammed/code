class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0]
        def dfs(root):
            if not root:return -1
            left = dfs(root.left)
            right=dfs(root.right)
            max_d[0]=max(max_d[0],left+right+2)
            return 1+max(left,right)
        dfs(root)
        return max_d[0]