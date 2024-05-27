/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function(nums) {
    nums.sort((a, b) => b - a);
    for (let i = 1; i <= nums.length; i++) {
        if (nums[i - 1] >= i && (i === nums.length || nums[i] < i)) {
            return i;
        }
    }
    return -1;
};