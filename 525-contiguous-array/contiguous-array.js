var findMaxLength = function(nums) {
    let count = 0;
    let maxLen = 0;
    let map = new Map();
    map.set(0, -1);
    for (let i = 0; i < nums.length; i++) {
        count += nums[i] === 1 ? 1 : -1;
        if (map.has(count)) {
            maxLen = Math.max(maxLen, i - map.get(count));
        } else {
            map.set(count, i);
        }
    }
    return maxLen;
};