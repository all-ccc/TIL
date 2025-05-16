const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim());

const T = Number(input[0]);
const adjList = [];

for (let i = 1; i <= T; i++) {
    const arr = input[i].split(' ').map(Number);
    adjList.push(arr);
}

function dfs(node, visited) {
    for (let n = 0; n < T; n++) {
        if (adjList[node][n] && !visited[n]) {
            visited[n] = 1;
            dfs(n, visited);
        }
    }

    return visited;
}

for (let i = 0; i < T; i++) {
    const visited = Array.from({length: T}, () => 0);

    console.log(...dfs(i, visited));
}
