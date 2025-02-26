function solution(board) {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const row = board.length;
    const col = board[0].length;
    let rx, ry;
    
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (board[i][j] === 'R') {
                rx = i;
                ry = j;
                break;
            }
        }
    }
    
    const queue = [[rx, ry, 0]];
    const visited = Array.from({length: row}, () => Array(col).fill(false));
    visited[rx][ry] = true;

    while (queue.length) {
        const [curX, curY, count] = queue.shift();
        
        if (board[curX][curY] === 'G') {
            return count;
        }
        
        for (let d = 0; d < 4; d++) {
            let nx = curX; // 몇 칸씩 이동할지 모르기 때문에
            let ny = curY;
            
            while (nx + dx[d] >= 0 && nx + dx[d] < row &&
                   ny + dy[d] >= 0 && ny + dy[d] < col &&
                   board[nx + dx[d]][ny + dy[d]] !== 'D'
          ) {
                nx += dx[d];
                ny += dy[d];
            }
            
            if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.push([nx, ny, count + 1]);
                }
        }
    }
    
    return -1;
}