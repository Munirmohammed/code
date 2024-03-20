var findJudge = function(n, trust) {
     var trust_counts = new Array(n + 1).fill(0);
        for(var i = 0; i < trust.length; i++) {
            trust_counts[trust[i][0]]--;
            trust_counts[trust[i][1]]++;
        }
        for(var i = 1; i <= n; i++) {
            if(trust_counts[i] === n - 1) {
                return i;
            }
        }
        return -1;
};