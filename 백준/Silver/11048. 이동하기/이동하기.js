const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [[N,M], ...map] = (require("fs").readFileSync(filePath).toString())
                        .trim()
                        .split("\n")
                        .map(line => line.split(" ").map(Number));

for (let i=0;i<N;i++) {
    for (let j=0;j<M;j++) {
        const left = (j-1) >= 0 ? map[i][j-1] : 0;
        const up = (i-1) >= 0 ? map[i-1][j] : 0;
        const topLeft = ((j-1) >= 0 && (i-1) >= 0) ? map[i-1][j-1] : 0;
        map[i][j] = Math.max(left, up, topLeft) + map[i][j]
    }
}

console.log(map[N-1][M-1]);