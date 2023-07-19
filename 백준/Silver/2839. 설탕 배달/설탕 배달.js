const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const N = Number((require("fs").readFileSync(filePath).toString()).trim());

const dp = Array(N+1).fill(0);
dp[3] = 1; dp[5] = 1;

for (let i=6;i<N+1;i++) {
    if (dp[i-5]) dp[i] = dp[i-5] + 1;
    else if (dp[i-3]) dp[i] = dp[i-3] + 1;
}

console.log(dp[N] ? dp[N] : -1);