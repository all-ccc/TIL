function solution(n, wires) {
    const adjList = Array.from({length: n + 1}, () => new Set());
    let result = n;
    
    for (let [a, b] of wires) {
        adjList[a].add(b);
        adjList[b].add(a);
    }
    
    for (let [a, b] of wires) { // 전선 하나씩 끊기
        adjList[a].delete(b);
        adjList[b].delete(a);
        
        const visited = Array(n + 1).fill(false);
        const cntA = dfs(a, visited);
        const cntB = n - cntA;
        
        result = Math.min(Math.abs(cntA - cntB), result);
        
        adjList[a].add(b); // 다시 복구
        adjList[b].add(a);
    }
    
    return result;
    
    function dfs(start, visited) {
        visited[start] = true;
        
        let cnt = 1;
        for (let next of adjList[start]) {
            if (!visited[next]) {
                cnt += dfs(next, visited);
            }
        }
        
        return cnt;
    }
    
}