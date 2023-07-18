function solution(maps) {
    const n = maps.length, m = maps[0].length;

    let q = [[0,0]];
    while (q.length) {
        const [x,y] = q.pop();

        for (const [dx,dy] of [[1,0], [-1,0], [0,1], [0,-1]]) {
            nx = x + dx; ny = y + dy;
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            
            if (maps[nx][ny] === 1) {
                maps[nx][ny] = maps[x][y] + 1;
                q.unshift([nx, ny]);
            }
        }
    }
    return maps[n-1][m-1] !== 1 ? maps[n-1][m-1] : -1;
}