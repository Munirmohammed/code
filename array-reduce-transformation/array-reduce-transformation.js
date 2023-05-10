var reduce = function(nums, fn, init) {
    ans = init
    for(const i of nums){
        ans = fn(ans , i)
        console.log(ans,i)
    }
    return ans
};