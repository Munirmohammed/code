/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let ct = init
    return{
    increment: () => ++ct,
    decrement: () => --ct,
    reset: () => ct = init
    }
};

