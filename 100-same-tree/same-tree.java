class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {
            return false;
        }
        
        LinkedList queueP = new LinkedList<>();
        LinkedList queueQ = new LinkedList<>();
        
        queueP.add(p);
        queueQ.add(q);
        
        while (!queueP.isEmpty() && !queueQ.isEmpty()) {
            TreeNode nodeP = (TreeNode) queueP.poll();
            TreeNode nodeQ = (TreeNode) queueQ.poll();
            
            if (nodeP.val != nodeQ.val) {
                return false;
            }
            
            if ((nodeP.left == null && nodeQ.left != null) || (nodeP.left != null && nodeQ.left == null)) {
                return false;
            }
            
            if ((nodeP.right == null && nodeQ.right != null) || (nodeP.right != null && nodeQ.right == null)) {
                return false;
            }
            
            if (nodeP.left != null) {
                queueP.add(nodeP.left);
            }
            
            if (nodeP.right != null) {
                queueP.add(nodeP.right);
            }
            
            if (nodeQ.left != null) {
                queueQ.add(nodeQ.left);
            }
            
            if (nodeQ.right != null) {
                queueQ.add(nodeQ.right);
            }
        }
        
        return queueP.isEmpty() && queueQ.isEmpty();
    }
}