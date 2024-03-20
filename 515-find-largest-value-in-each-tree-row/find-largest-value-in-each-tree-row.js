var largestValues = function(root) {
    if (!root) {
        return [];
    }

    let queue = [root];
    let res = [];
    while (queue.length) {
        let levelSize = queue.length;
        let maxVal = -Infinity;
        for (let i = 0; i < levelSize; i++) {
            let node = queue.shift();
            maxVal = Math.max(maxVal, node.val);
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
        res.push(maxVal);
    }
    return res;
};