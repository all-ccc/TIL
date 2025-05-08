const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim());

const [N, M] = input[0].split(' ').map(Number);
const adjList = Array.from({length: N + 1}, () => []);
const visited = Array(N + 1).fill(false);
let result = 0;

for (let i = 1; i <= M; i++) {
    let [a, b] = input[i].split(' ').map(Number);
    adjList[a].push(b);
    adjList[b].push(a);
}

const queue = [];

for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
        bfs(i);
        result++;
    }
}


function bfs(node) {
    queue.push(node);
    visited[node] = true;

    while (queue.length > 0) {
        const now = queue.shift();
        
        for (let next of adjList[now]) {
            if (!visited[next]) {
                queue.push(next);
                visited[next] = true;
            }
        }
    }
}

console.log(result);


