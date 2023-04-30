/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    ans = init
    for(const i of nums){
        ans = fn(ans , i)
        console.log(ans,i)
    }
    return ans
};