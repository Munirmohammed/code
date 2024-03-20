var isSameTree = function(p, q) {
    if (p === null && q === null) {
        return true;
    }
    if (p === null || q === null) {
        return false;
    }
    
    let queueP = [p];
    let queueQ = [q];
    
    while (queueP.length > 0 && queueQ.length > 0) {
        let nodeP = queueP.shift();
        let nodeQ = queueQ.shift();
        
        if (nodeP.val !== nodeQ.val) {
            return false;
        }
        
        if ((nodeP.left === null && nodeQ.left !== null) || (nodeP.left !== null && nodeQ.left === null)) {
            return false;
        }
        
        if ((nodeP.right === null && nodeQ.right !== null) || (nodeP.right !== null && nodeQ.right === null)) {
            return false;
        }
        
        if (nodeP.left !== null) {
            queueP.push(nodeP.left);
        }
        
        if (nodeP.right !== null) {
            queueP.push(nodeP.right);
        }
        
        if (nodeQ.left !== null) {
            queueQ.push(nodeQ.left);
        }
        
        if (nodeQ.right !== null) {
            queueQ.push(nodeQ.right);
        }
    }
    
    return queueP.length === 0 && queueQ.length === 0;
};