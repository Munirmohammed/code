var findJudge = function(n, trust) {
     var trustCounts = new Array(n + 1).fill(0);
        for(var i = 0; i < trust.length; i++) {
            trustCounts[trust[i][0]]--;
            trustCounts[trust[i][1]]++;
        }
        for(var i = 1; i <= n; i++) {
            if(trustCounts[i] === n - 1) {
                return i;
            }
        }
        return -1;
};