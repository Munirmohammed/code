var findJudge = function(n, trust) {
    var graph = new Array(n + 1).fill(0).map(() => []);
    for(var i = 0; i < trust.length; i++) {
        graph[trust[i][0]].push(trust[i][1]);
    }
    for(var i = 1; i <= n; i++) {
        if(graph[i].length === 0) {
            var count = 0;
            for(var j = 1; j <= n; j++) {
                if(i !== j && graph[j].includes(i)) {
                    count++;
                }
            }
            if(count === n - 1) {
                return i;
            }
        }
    }
    return -1;
};