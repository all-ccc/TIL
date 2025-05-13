const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim());

const N = Number(input[0]);
const grid1 = [];
const grid2 = [];

let count1 = 0; // 적록색약 X
let count2 = 0; // 적록색약 O

const dx = [0, 0, -1, 1];
const dy = [1, -1, 0, 0];

for (let i = 1; i <= N; i++) {
    const row = input[i].split('');
    grid1.push(row);
    grid2.push(row.map(c => c === 'G' ? 'R' : c));
}

function bfs(n, m, visited, grid) {
    visited[n][m] = true;
    const queue = [[n, m]];

    while (queue.length > 0) {
        let [x, y] = queue.shift();

        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (
                nx >= 0 && nx < N &&
                ny >= 0 && ny < N &&
                !visited[nx][ny] &&
                grid[x][y] === grid[nx][ny]
            ) {
                visited[nx][ny] = true;
                queue.push([nx, ny]);
            }
        }
    }
}

const visited1 = Array.from({length: N}, () => Array(N).fill(false));
const visited2 = Array.from({length: N}, () => Array(N).fill(false));

for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (!visited1[i][j]) {
            bfs(i, j, visited1, grid1);
            count1++;
        }
        if (!visited2[i][j]) {
            bfs(i, j, visited2, grid2);
            count2++;
        }
    }
}

console.log(count1, count2);