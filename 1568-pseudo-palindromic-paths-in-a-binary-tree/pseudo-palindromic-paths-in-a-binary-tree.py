class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans=0
        def search(node,even):
            if node==None:
                return
            even[node.val]= not even[node.val]
            if node.left==None and node.right==None:
                if sum(even)<=1:
                    nonlocal ans
                    ans+=1
            else:
                search(node.left,even)
                search(node.right,even)
            even[node.val]= not even[node.val]
        search(root,[False]*10)
        return ans                    