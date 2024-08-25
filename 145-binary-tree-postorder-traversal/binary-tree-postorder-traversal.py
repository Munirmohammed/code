class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        num=[]
        def f(root):
            if root==None: return num
            f(root.left)
            f(root.right)
            num.append(root.val)
            return num
        return f(root)