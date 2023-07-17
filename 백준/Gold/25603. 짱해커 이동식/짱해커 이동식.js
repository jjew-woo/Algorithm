const [[N, K], cost] = (require("fs").readFileSync("/dev/stdin").toString()
    )
    .trim()
    .split("\n")
    .map(line => line.split(" ").map(Number));

let s = 0, minCost = cost[0], ans = cost[0];
let minIdx;
for (let i=s; i < s+K; i++) {
    if (cost[i] <= minCost) {
        minIdx = i;
        minCost = cost[i]
        ans = minCost
    }
}
s = minIdx + 1;

let q, i, minWindow, minWindowIdx;
while (s+K <= N) {
    q = [];
    i = s;
    minWindow = 0

    for (let j=i; j < N; j++) {
        if (cost[j] <= ans) {
            s = j + 1;
            break;
        } 
        else {
            q.push(cost[j]);
            if (minWindow === 0) {
                minWindow = cost[j];
                minWindowIdx = j;
            }
            else {
                if (cost[j] <= minWindow) {
                    minWindow = cost[j];
                    minWindowIdx = j;
                }
            }

            if (q.length >= K) {
                s = minWindowIdx + 1;
                ans = minWindow;
                break;
            } 
        }
    }
}

console.log(ans);