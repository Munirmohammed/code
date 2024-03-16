var findMaxLength = function(nums) {
    let maxLen = 0;
    let count = 0;
    let counts = new Map();
    counts.set(0, -1);
    for (let i = 0; i < nums.length; i++) {
        count += nums[i] === 1 ? 1 : -1;
        if (counts.has(count)) {
            maxLen = Math.max(maxLen, i - counts.get(count));
        } else {
            counts.set(count, i);
        }
    }
    return maxLen;
};