function solution(n, edge) {
    const adjList = Array.from({length: n + 1}, () => []);
    
    for (let i = 0; i < edge.length; i++) {
        let a = edge[i][0];
        let b = edge[i][1];
        adjList[a].push(b);
        adjList[b].push(a);
        
    }
    // bfs -> 최단 거리 구하고 -> 가장 멀리 떨어진 노드 개수 return
    const distance = Array(n + 1).fill(-1);
    const queue = [1];
    distance[1] = 0;
    
    while (queue.length) {
        const now = queue.shift();
        
        for (let node of adjList[now]) {
            if (distance[node] === -1) {
                distance[node] = distance[now] + 1;
                queue.push(node);
            }
        }
    }
    
    const maxDis = Math.max(...distance);
    
    return distance.filter(d => d === maxDis).length;
    
}