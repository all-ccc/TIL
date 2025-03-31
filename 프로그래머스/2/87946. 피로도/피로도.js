function solution(k, dungeons) {
    let result = 0;
    const visited = [false];
    
    function dfs(power, cnt) {
        result = Math.max(result, cnt);
        
        for (let i = 0; i < dungeons.length; i++) {
            const [minPower, need] = dungeons[i];
            
            if (!visited[i] && minPower <= power) {
                visited[i] = true;
                dfs(power - need, cnt + 1);
                visited[i] = false;
            }
        }
    }
    
    dfs(k, 0);
    
    return result;
}