var reverseList = function(head) {
    if (head === null) {
        return null;
    }

    let nodes = [];
    let current = head;
    while (current !== null) {
        nodes.push(current);
        current = current.next;
    }

    for (let i = nodes.length - 1; i >= 0; i--) {
        nodes[i].next = i === 0 ? null : nodes[i - 1];
    }

    return nodes[nodes.length - 1];
};