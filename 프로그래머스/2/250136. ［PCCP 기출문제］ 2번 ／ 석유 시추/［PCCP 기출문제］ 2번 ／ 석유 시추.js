function solution(land) {
    const row = land.length;
    const col = land[0].length;
    const dr = [0, 0, -1, 1];
    const dc = [1, -1, 0, 0];
    
    const oilPerCol = Array(col).fill(0);
    const visited = Array.from({length: row}, () => Array(col).fill(false));
    
    for (let r = 0; r < row; r++) {
        for (let c = 0; c < col; c++) {
            if (land[r][c] === 1 && !visited[r][c]) {
                const checkCol = new Set([c]);
                let oilAmount = 1;
                const queue = [[r, c]];
                visited[r][c] = true;
                
                while (queue.length > 0) {
                    const [nowR, nowC] = queue.shift();
                    for (let i = 0; i < 4; i++) {
                        const nr = nowR + dr[i];
                        const nc = nowC + dc[i];
                    
                        if (nr >= 0 && nr < row &&
                            nc >= 0 && nc < col &&
                            land[nr][nc] === 1 &&
                            !visited[nr][nc]
                       ) {
                            queue.push([nr, nc]);
                            visited[nr][nc] = true;
                            checkCol.add(nc);
                            oilAmount++;
                        }   
                    }
                }
                
                for (let col of checkCol) {
                    oilPerCol[col] += oilAmount;
                }
                
            }
        }
    }
    
    return Math.max(...oilPerCol);
    
}