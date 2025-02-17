function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, 1, -1];
    
    // if (maps[n-2][m-1] === 0 && maps[n-1][m-2] === 0) return -1;
    
    queue = [];
    queue.push([0, 0, 1]); // x좌표, y좌표, 이동거리
    
    while (queue.length > 0) {
        let [x, y, move] = queue.shift();
        
        if (x === n - 1 && y === m - 1) return move;
        
        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] === 1) {
                queue.push([nx, ny, move + 1]);
                maps[nx][ny] = 0; // 방문 표시
                
            }
        }
    }
    
    return -1;
    
}