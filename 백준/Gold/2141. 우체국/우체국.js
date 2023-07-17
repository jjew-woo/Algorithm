const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [[N], ...town] = (require("fs").readFileSync(filePath).toString())
                        .trim()
                        .split("\n")
                        .map(line => line.split(" ").map(Number));

let sum = town.reduce((acc, cur) => acc+cur[1], 0), now = 0;
town.sort((a,b) => a[0]-b[0]);

for (let i=0; i<N;i++) {
    now += town[i][1];
    if (now >= sum/2) {
        console.log(town[i][0]);
        break;
    }
}