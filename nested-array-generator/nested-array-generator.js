var inorderTraversal = function*(arr) {
    let array = arr.flat(Infinity)
    array.reverse()
    while(array.length) {
        yield array.pop()
    }
};
