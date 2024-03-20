func largestValues(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }

    queue := []*TreeNode{root}
    res := []int{}
    for len(queue) > 0 {
        levelSize := len(queue)
        maxVal := queue[0].Val // Initialize maxVal to the value of the first node in the queue
        for i := 0; i < levelSize; i++ {
            node := queue[0]
            queue = queue[1:]
            if node.Val > maxVal {
                maxVal = node.Val
            }
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        res = append(res, maxVal)
    }
    return res
}