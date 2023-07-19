const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const [[N,M], ...map] = (require("fs").readFileSync(filePath).toString())
                        .trim()
                        .split("\n")
                        .map(line => line.split(" ").map(Number));

const sum = Array.from(new Array(N), () => new Array(M).fill(0));
const visited = Array.from(new Array(N), () => new Array(M).fill(false));
sum[0][0] = map[0][0];

const q = [[0,0]];
while (q.length) {
    [x, y] = q.shift();
    visited[x][y] = true;

    for ([dx, dy] of [[1,0], [0,1], [1,1]]) {
        nx = x + dx; ny = y + dy;

        if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

        sum[nx][ny] = Math.max(sum[nx][ny], sum[x][y]+map[nx][ny]);
        if (!visited[nx][ny]) {
            visited[nx][ny] = true;
            q.push([nx,ny]);
        }
    }
}

console.log(sum[N-1][M-1]);