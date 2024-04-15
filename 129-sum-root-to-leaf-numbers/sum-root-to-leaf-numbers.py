class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root,curr):
            nonlocal ans
            if not root:
                return ""

            curr+=str(root.val)
            if not root.left and not root.right:
                ans+=int(curr)
            dfs(root.left,curr)
            dfs(root.right,curr)

        dfs(root,"")
        return ans