const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim());

const N = Number(input[0]);
const area = [];
let maxNum = -1;

for (let i = 1; i <= N; i++) {
    const row = input[i].split(' ').map(Number);
    const max = Math.max(...row);
    if (max > maxNum) maxNum = max;
    area.push(row);
}

let result = 0;
const dx = [0, 0, -1, 1];
const dy = [1, -1, 0, 0];

for (let height = 0; height < maxNum; height++) {
    let safeZone = 0;
    const visited = Array.from({length: N}, () => Array(N).fill(false));

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (!visited[i][j] && area[i][j] > height) { // 방문하지 않았고 안전영역이라면면
                visited[i][j] = true;
                bfs(i, j, height, visited);
                safeZone++;
            }
        }
    }

    if (safeZone > result) result = safeZone;
}


function bfs(x, y, h, visited) {
    const queue = [[x, y]];
    while (queue.length > 0) {
        let [nowX, nowY] = queue.shift();

        for (let i = 0; i < 4; i++) {
            let nextX = nowX + dx[i];
            let nextY = nowY + dy[i];
    
            if (
                nextX >= 0 && nextX < N &&
                nextY >= 0 && nextY < N &&
                !visited[nextX][nextY] &&
                area[nextX][nextY] > h
            ) {
                queue.push([nextX, nextY]);
                visited[nextX][nextY] = true;
            }
        }
    }
    
}

console.log(result);

