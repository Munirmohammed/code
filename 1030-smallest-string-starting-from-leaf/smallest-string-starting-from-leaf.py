class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = "z" * (8500 + 1)  # Initialize with a string lexicographically larger than any possible result

        def dfs(node, path):
            if not node:
                return
            path = chr(node.val + ord('a')) + path  # Prepend the current node's value to the path
            if not node.left and not node.right:  # If the current node is a leaf
                self.res = min(self.res, path)  # Update the result with the lexicographically smallest path
            dfs(node.left, path)  # Traverse the left subtree
            dfs(node.right, path)  # Traverse the right subtree

        dfs(root, "")
        return self.res