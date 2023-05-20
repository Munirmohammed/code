class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_depth(node,l):
            if node is None:
                return l
            l += 1
            return max(find_depth(node.left,l),find_depth(node.right,l))
        return find_depth(root,0)


