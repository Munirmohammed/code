function memoize(fn) {
    const root = new Map();
    return function (...args) {
        let node = root;
        for (const arg of args) {
            if(!node.has(arg)) node.set(arg, new Map());
            node = node.get(arg);
        }
        if (!node.has("__CACHE__")) node.set("__CACHE__", fn(...args));
        return node.get("__CACHE__");
    }
}
