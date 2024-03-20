class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue, res = [root], []
        while queue:
            max_val = float('-inf')
            for i in range(len(queue)):
                node = queue.pop(0)
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_val)
        return res