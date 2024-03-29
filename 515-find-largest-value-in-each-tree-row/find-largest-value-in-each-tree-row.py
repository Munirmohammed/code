class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue, res = [root], []
        while queue:
            level_size = len(queue)
            max_val = float('-inf')
            for _ in range(level_size):
                node = queue.pop(0)
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_val)
        return res