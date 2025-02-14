function solution(n, computers) {
    let result = 0;
    let visited = [false];

    function dfs(i) {
        visited[i] = true;
        
        for (let k = 0; k < computers[i].length; k++) {
            if (computers[i][k] === 1 && !visited[k]) {
                dfs(k);
            }
        }
    }
    
    for (let i = 0; i < computers.length; i++) {
        if (!visited[i]) {
            dfs(i);
            result += 1;
        }
    }
    
    return result;

}