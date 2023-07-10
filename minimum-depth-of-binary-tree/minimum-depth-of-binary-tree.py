class Solution(object):
    def minDepth(self, root):
        if root is None:  return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if root.left is None and root.right is None:
            return 1
        
        if root.left is None:
            return 1 + rightDepth

        if root.right is None:
            return 1 + leftDepth
       
        return min(leftDepth, rightDepth) + 1;