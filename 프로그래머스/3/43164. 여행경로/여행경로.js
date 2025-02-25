function solution(tickets) {
    const len = tickets.length;
    const visited = Array(len).fill(false);
    let result = [];
    
    function dfs(route) {
        if (route.length === len + 1) {
            result.push(route);
            return;
        }
        
        for (let i = 0; i < len; i++) {
            const [start, end] = tickets[i];
            
            if (!visited[i] && route[route.length - 1] === start) {
                visited[i] = true;
                dfs([...route, end]);
                visited[i] = false;
            }
        }
    }
    dfs(['ICN']);
    
    return result.sort()[0];
}